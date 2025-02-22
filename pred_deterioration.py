# -*- coding: utf-8 -*-
"""Pred_deterioration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/rdestenay/oldpicsrestoration/blob/master/Pred_deterioration.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# %reload_ext autoreload
# %autoreload 2

from fastai.vision import *

df = pd.read_csv('deteriorated/data.csv')
df.head()

tfms = get_transforms()

data = (ImageItemList.from_df(df, path='deteriorated')
        .random_split_by_pct()
        .label_from_df(cols=[1,2])
        .transform(tfms, size=128)
        .databunch())

data.show_batch(rows=2, figsize=(9,7))

learn2 = create_cnn(data, models.resnet34, metrics=root_mean_squared_error)
learn2.fit_one_cycle(1)

learn.unfreeze()
learn.fit_one_cycle(1, slice(1e-5,3e-4), pct_start=0.05)

pred = learn.get_preds()

pred

((pred[0].squeeze()-pred[1])**2).mean().sqrt()

pred2 = learn2.get_preds()

pred2[1]

