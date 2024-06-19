# ベースイメージとして最新のUbuntuを使用
FROM ubuntu:latest

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    gdb \
    cmake \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workdir

# コンテナ起動時に実行されるデフォルトコマンド
CMD ["/bin/bash"]
