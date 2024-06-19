1. **Dockerfileの作成**:

    ```Dockerfile
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
    ```

2. **Dockerイメージのビルド**:
   Dockerfileがあるディレクトリに移動し、以下のコマンドを実行します。

    ```sh
    docker build -t cpp-dev-environment .
    ```

3. **コンテナの起動**:
   ビルドしたDockerイメージを使用してコンテナを起動します。

    ```sh
    docker run -it --rm -v $(pwd):/workdir cpp-dev-environment
    ```

   `-v $(pwd):/workspace`オプションは、現在のディレクトリをコンテナの`/workspace`ディレクトリにマウントするためのもので、ホストとコンテナ間でファイルを共有するために使用します。

4. **C++プログラムの作成とコンパイル**:
   コンテナ内でC++のソースファイルを作成し、コンパイルして実行します。

    ```sh
    # コンテナ内で以下のコマンドを実行
    cd /workspace
    nano hello.cpp
    ```

    以下の簡単なC++プログラムを`hello.cpp`に書き込みます。

    ```cpp
    #include <iostream>

    int main() {
        std::cout << "Hello, Docker!" << std::endl;
        return 0;
    }
    ```

    保存してエディタを閉じたら、次のコマンドでコンパイルします。

    ```sh
    g++ -o hello hello.cpp
    ./hello
    ```

    "Hello, Docker!"と出力されれば成功です。

