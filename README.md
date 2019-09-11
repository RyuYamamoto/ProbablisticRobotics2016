 ProbablisticRobotics2016
=================

[![Build Status](https://travis-ci.org/RyuYamamoto/ProbablisticRobotics2016.svg?branch=master)](https://travis-ci.org/RyuYamamoto/ProbablisticRobotics2016)

### LICENSE
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)  
This software is released under the MIT License, see LICENSE.  

### 問題
強化学習による迷路探索．デフォルトでは10×15マスの迷路を探索する．

![map](picture/map.jpg)  

### ルール
 - 赤い四角がエージェントであり，白いマスが通れる経路，青いマスが通れるが報酬がマイナスとなる経路(ペナルティ)，黄色いマスがゴール．  
 - エージェントは左上マスからスタートし，右下黄色マスのゴールを目指し経路を探索する．  
 - ゴールに到達すると報酬が与えられる．エージェントはなるべく報酬がマイナスとなる経路を避けつつ，全体として報酬が最大となるような経路を探索する．  
 - Q-Learningによる学習．学習率は0.2，割引率は0.9とした．  
 - 行動選択はε-greedy法．  

### ソフトウェア
 - main.py  
   - メインコード．  
 - map_display.py  
   - pygameによる可視化．  
 - QLearning.py
   - QLearningによる行動学習  
 - data/map.csv  
   - 各セルの報酬情報.  

### 外部ライブラリ
 - numpy  
 - matplotlib  
 - pygame  

### 仕様
 - 300回ゴールしたら学習を終了，最適方策を可視化したものをpolicy.jpgという画像名で保存．各マスの矢印は最適な行動を示し，各セルのQ値の大きさによってマスの色が変わる(Q値が大きいほど赤色になる．Q値がゼロの場合は変化なし)．  
 - --testの引数をつけることによりGUI無しで動作確認可能(主にTravis-CI向け)．  

### 結果
最終的に得られた方策．  

![policy](picture/policy.jpg)  


Q値の変化1試行毎のQ値の最大値をプロットした．一回のマスの移動を1試行とする．下図でQ値が跳ね上がっている部分はゴールに到達した場合であり，試行回数が増えるにつれてQ値の値が大きくなり，ゴールに到達する頻度が増えていくことがわかる．  

![q_value](picture/q_value.jpg)  

動いている様子

[![](http://img.youtube.com/vi/eK2_nBD0hzY/0.jpg)](https://www.youtube.com/watch?v=eK2_nBD0hzY)

### おまけ
data/map.csvをいじれば何×何でも探索可能．ただマスが増えると収束させるために試行回数をより増やす必要がある．

#### 20×30の場合
![q_value](picture/policy20x30.jpg)  

#### 100×100の場合(計算終わる気がしなかった)
![q_value](picture/map100x100.png)  
