 ProbablisticRobotics2016
=================

[![Build Status](https://travis-ci.org/RyuYamamoto/ProbablisticRobotics2016.svg?branch=master)](https://travis-ci.org/RyuYamamoto/ProbablisticRobotics2016)

### 問題
強化学習による迷路探索．デフォルトでは10×15マスの迷路を探索する．

### ルール
 - 白いマスが通れる経路，黒いマスが通れるが報酬がマイナスとなる経路(ペナルティ)，青いマスがゴール．  
 - ゴールに到達すると報酬が与えられる．エージェントはなるべく報酬がマイナスとなる経路を避けつつ，ゴールを目指しながら報酬が最大となるような経路を探索する．  

### ソフトウェア
 - main.py  
  - メインコード．  
 - map_display.py  
  - pygameによる可視化．  
 - QLearning.py
  - QLearningによる行動学習  
 - data/map.csv  
  - 各セルの報酬情報.  

### 仕様
 - 300回ゴールした学習を終了，方策を可視化したものをpolicy.jpgという画像で保存．最適な行動だけでなく各セルのQ値の大きさによってマスの色が変わる．  
