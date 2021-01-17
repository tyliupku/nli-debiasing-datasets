# nli-debiasing-datasets
CoNLL 2020 "An Empirical Study on Model-agnostic Debiasing Strategies for Robust Natural Language Inference"

The benchmark adversarial datasets used in our paper contain 114,754 instances, with 3-way classification 'entailment'/'contradiction'/'neutral'. We merge all the datasets to a file 'robust_nli.txt', to test your model on this benchmark, simply run 

```
python --pred prediction.txt --src "robust_nli.txt"
```

'prediction.txt' is the model output file, with label 'entailment'/'contradiction'/'neutral'. One label per line is the model prediction for corresponding instance in 'robust_nli.txt'. 'random_prediction.txt' is a random prediction output.

The benchmark dataset 'robust_nli.txt' is also available on [Google Drive](https://drive.google.com/file/d/1-domFwWuBXEXmmOZ64MHVDxaAkmhOY21/view?usp=sharing).

For details of the benchmark adversarial datasets, please to refer to [our paper](https://www.aclweb.org/anthology/2020.conll-1.48.pdf).

## Results
| Model | Avg  |
| ------ | --------- |
| InferSent | 51.7 |
| DAM | 55.0 |
| ESIM | 60.1 |
| BERT(base) | 72.4 |
| XLNet(base) | 75.9 |
| RoBERTa(base) | 77.8 |

## Citation

If you use our NLI debiasing method, please consider citing our work:

```
@inproceedings{liu-etal-2020-empirical,
    title = "An Empirical Study on Model-agnostic Debiasing Strategies for Robust Natural Language Inference",
    author = "Liu, Tianyu  and
      Xin, Zheng  and
      Ding, Xiaoan  and
      Chang, Baobao  and
      Sui, Zhifang",
    booktitle = "Proceedings of the 24th Conference on Computational Natural Language Learning",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.conll-1.48",
    doi = "10.18653/v1/2020.conll-1.48",
    pages = "596--608",
}
```
