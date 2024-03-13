FROM ubuntu:latest

RUN apt update && apt install -y \
  curl \
  bzip2 \
  ca-certificates \
  make \
  tmux

RUN curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

RUN ./bin/micromamba shell init -s bash -p ~/micromamba

COPY environment.yml .
RUN ./bin/micromamba create -y -f environment.yml
RUN rm environment.yml

CMD ["/bin/bash"]
