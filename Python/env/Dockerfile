FROM continuumio/anaconda3

RUN apt-get update
RUN pip install --upgrade pip

WORKDIR /workdir

ENTRYPOINT ["jupyter-lab", "--NotebookApp.ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='mNFIjfSjfIf/Cd/PTe4h/cgboVXIUBszH5MxU8o7rFg'", "--NotebookApp.allow_origin='*'"]

CMD ["--notebook-dir=/workdir"]



