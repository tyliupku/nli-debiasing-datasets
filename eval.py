import codecs
import json
import os
from collections import defaultdict
import numpy as np
import argparse


def eval(pred_path, src_path):
    Tri_dataset = ["IS_CS", "LI_LI", "PI_CD", "PI_SP", "ST_LM", "ST_NE", "ST_SE", "ST_WO"]
    Ent_bin_dataset = ["IS_SD"]
    Con_bin_dataset = ["LI_TS"]
    eps = 1e-9
    split_len = defaultdict(float)
    split_true = defaultdict(float)

    assert os.path.isfile(pred_path), "prediction file does not exist"
    assert os.path.isfile(src_path), "src file does not exist"

    fsrc = codecs.open(src_path, "r", encoding="utf-8").read().strip().split("\n")
    fpred = [x.lower() for x in codecs.open(pred_path, "r", encoding="utf-8").read().strip().split("\n")]

    assert len(fsrc) == len(fpred), "pred file length mismatches"
    assert all([pred in ["contradiction", "entailment", "neutral"] for pred in fpred]), \
        "pred label must in \'contradiction\', \'entailment\' or \'neutral\'"

    for src, pred in zip(fsrc, fpred):
        example = json.loads(src)
        split, glabel = example['split'], example['label']
        split_len[split] += 1
        glabel_list = [glabel]
        if split in Ent_bin_dataset:
            if glabel == "non-entailment":
                glabel_list = ["neutral", "contradiction"]
        elif split in Con_bin_dataset:
            if glabel == "non-contradiction":
                glabel_list = ["entailment", "neutral"]
        if pred in glabel_list:
            split_true[split] += 1

    all_dataset = Tri_dataset + Ent_bin_dataset + Con_bin_dataset
    for split in all_dataset:
        split_true[split] /= (split_len[split]+eps)
        print("{} : {}".format(split, split_true[split]))
    print("\nAvg : {}".format(np.mean(list(split_true.values()))))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", default="prediction.txt")
    parser.add_argument("--src", default="robust_nli.txt")
    args = parser.parse_args()
    eval(args.pred, args.src)
