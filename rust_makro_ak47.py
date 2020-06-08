from mouse import move
from win32api import GetKeyState
from keyboard import is_pressed


kordinatlarX = [-4.40,-12.40,-15.20,-14.40,-13.60,0.00,8.80,13.20,20.00,20.00,19.20,16.80,14.00,8.40,
-4.00,-6.00-11.20,-19.20,-18.80,-21.20,-20.00,-19.20,-16.00,-11.20,-4.00,4.00,17.60,20.00,22.00,26.00]

kordinatlarY = [8.40,24.00,20.00,20.00,17.60,15.60,12.40,12.00,8.00,6.40,6.00,7.20,8.80,13.60,15.20,16.00,
15.20,15.20,13.20,10.00,9.20,4.00,5.60,8.00,8.00,10.00,16.00,12.80,14.80,16.00]

xy = 0

gecikme = 0.129

print("Açma Kapama Tuşunu Seç")
tuş = input("")


aktifmi = False


def fare_basili():
    sol_tik = GetKeyState(0x01)
    return sol_tik < 0


print("Macro Çalıştırıldı") 
if aktifmi:
    print("Açık")
else:
    print("Kapalı")

son_durum = False
while True:
    aktif_ise = is_pressed(tuş)
    if aktif_ise != son_durum:
        son_durum = aktif_ise
        if son_durum:
            aktifmi = not aktifmi
            if aktifmi:
                print("Açık")
            else:
                print("Kapalı")

    if fare_basili() and aktifmi:
        while True:
            if fare_basili() and aktifmi:
                move(kordinatlarX[xy], kordinatlarY[xy], absolute=False, duration=gecikme)
                xy += 1
                if len(kordinatlarX) == xy:
                    xy = 0
            else:
                xy = 0