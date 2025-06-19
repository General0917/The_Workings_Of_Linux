#!/usr/bin/python3
import signal
# SIGINTシグナルを無視するように設定。第1引数にはハンドラを設定するシグナル(ここではsignal.SIGINT)を、
# 第2引数にはシグナルハンドラ(ここではsignal.SIG_IGN)を指定する。
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    pass
# 無限ループを実行して、SIGINTシグナルが無視されることを確認する。
# Ctrl+Cを押しても何も起こらないはず。
# このスクリプトを実行した後、Ctrl+Cを押してもプロセスは終了しないことを確認してください。
# 終了するには、Ctrl+Zでプロセスを停止し、`kill %1`でプロセスを終了させるか
