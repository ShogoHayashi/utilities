"""
Created on Thu Jan 26 2023
@author: ShogoHayashi
"""

import scipy
import matplotlib.pyplot as plt


# 展開前の伝達関数
def a():
    # 伝達関数の構築
    # ZerosPolesGainは([零点], [根], ゲイン(k))とする。
    G = scipy.signal.ZerosPolesGain([1, 2], [3, 4], 5)
    
    # ltiも同様
    # G = scipy.signal.lti([1, 2], [3, 4], K)


    # 上で作成したインスタンスを引数に与える。
    # w : 1次元周波数配列[rad/s]
    # mag : 1次元振幅配列[dB]
    # phase : 1次元位相配列[°]
    w, mag, phase = scipy.signal.bode(G)

    # 描画
    draw(w, mag, phase)



# 展開後の伝達関数
def b():
    # 伝達関数
    # TransferFunctionは([分子の係数], [分母の係数])とする。
    num = [1, 3, 3]
    den = [1, 2, 1]
    G = scipy.signal.TransferFunction(num, den)
    
    # ltiも同様
    # G = scipy.signal.lti(num, den)

    # ボード線図の計算
    w, mag, phase = scipy.signal.bode(G)
    
    # 描画
    draw(w, mag, phase)

def draw(w, mag, phase):
    # ゲイン線図の描画
    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)
    plt.ylabel("Gain[dB]")
    plt.grid()
    
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)
    plt.xlabel("w[rad/sec]")
    plt.ylabel("Phase[deg]")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    a()
    b()