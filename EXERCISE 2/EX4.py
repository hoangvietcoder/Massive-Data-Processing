from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

TAIXE = Table('TAIXE', metadata, Column('MATX', String, primary_key=True), Column('HOTEN', String),
              Column('SDT', String), Column('DIEMTB', Float), Column('LOAIXE', String), )
KH = Table('KH', metadata, Column('MAKH', String, primary_key=True), Column('HOTEN', String), Column('SDT', String))
DATXE = Table('DATXE', metadata, Column('MADX', String, primary_key=True),
              Column('MAKH', String, ForeignKey('KH.MAKH')), Column('DDI', String), Column('DDEN', String),
              Column('LXE', String), Column('KC', String), Column('GIA', Integer),
              Column('TGDAT', DateTime, default=datetime.utcnow()))
DOIXE = Table('DOIXE', metadata, Column('MADX', String, primary_key=True),
              Column('MATX', String, ForeignKey('TAIXE.MATX')), Column('TGBDAU', DateTime, default=datetime.utcnow()),
              Column('TGKTHUC', DateTime, default=datetime.utcnow(), nullable=True),
              Column('KQUA', String, nullable=True))
CHUYENDI = Table('CHUYENDI', metadata, Column('MACD', String, primary_key=True),
                 Column('MADX', String, ForeignKey('DOIXE.MADX')), Column('MATX', String, ForeignKey('DOIXE.MATX')),
                 Column('TGDI', DateTime, default=datetime.utcnow()),
                 Column('TGDEN', DateTime, default=datetime.utcnow(), nullable=True),
                 Column('GIA', Integer, nullable=True),
                 Column('HTTTOAN', String, nullable=True), Column('DIEM', Float, nullable=True))
metadata.create_all(engine)

conn = engine.connect()

conn.execute(TAIXE.insert(), [
    {'MATX': 'TX001', 'HOTEN': 'Mai Hoang Viet', 'SDT': '0971600213', 'DIEMTB': 8.3, 'LXE': 'McLaren Senna'},
    {'MATX': 'TX002', 'HOTEN': 'Mai Tan Hoang', 'SDT': '0988948749', 'DIEMTB': 3.2, 'LXE': 'Mercedes-Benz'},
    {'MATX': 'TX005', 'HOTEN': 'Huynh Thi Thanh Thao', 'SDT': '0387200281', 'DIEMTB': 6.5, 'LXE': 'Lamborghini'},
])

conn.execute(KH.insert(), [
    {'MAKH': 'KH001', 'HOTEN': 'Nguyen Van C', 'SDT': '0973123456'},
    {'MAKH': 'KH002', 'HOTEN': 'Nguyen Van A', 'SDT': '0963654321'},
    {'MAKH': 'KH003', 'HOTEN': 'Nguyen Van B', 'SDT': '0951234567'}
])

conn.execute(DATXE.insert(), [
    {'MADX': 'DX001', 'MAKH': 'KH001', 'DDI': 'An Giang', 'DDEN': 'TP.HCM', 'LXE': 'Toyota', 'KC': '230km',
     'GIA': 2000000},
    {'MADX': 'DX002', 'MAKH': 'KH002', 'DDI': 'Tay Ninh', 'DDEN': 'Ha Noi', 'LXE': 'Honda', 'KC': '500km',
     'GIA': 4200000},
    {'MADX': 'DX003', 'MAKH': 'KH003', 'DDI': 'Tien Giang', 'DDEN': 'TP.HCM', 'LXE': 'Yamaha', 'KC': '100km',
     'GIA': 1300000},
    {'MADX': 'DX004', 'MAKH': 'KH002', 'DDI': 'Ha Noi', 'DDEN': 'Dong Thap', 'LXE': 'Suzuki', 'KC': '200km',
     'GIA': 5500000},
    {'MADX': 'DX005', 'MAKH': 'KH003', 'DDI': 'Binh Dinh', 'DDEN': 'Quang Ngai', 'LXE': 'Tesla', 'KC': '300km',
     'GIA': 1000000},
    {'MADX': 'DX006', 'MAKH': 'KH001', 'DDI': 'Kien Giang', 'DDEN': 'TP.HCM', 'LXE': 'BMW', 'KC': '240km',
     'GIA': 2100000}
])

conn.execute(DOIXE.insert(), [
    {'MADX': 'DX001', 'MATX': 'TX001', 'KQUA': 'THANH CONG'},
    {'MADX': 'DX002', 'MATX': 'TX002', 'KQUA': 'KHACH HANG HUY'},
    {'MADX': 'DX003', 'MATX': 'TX005', 'KQUA': 'TAI XE HUY'},
    {'MADX': 'DX004', 'MATX': 'TX001', 'KQUA': 'THANH CONG'},
    {'MADX': 'DX005', 'MATX': 'TX002', 'KQUA': 'KHACH HANG HUY'},
    {'MADX': 'DX006', 'MATX': 'TX005', 'KQUA': 'TAI XE HUY'}
])

conn.execute(CHUYENDI.insert(), [
    {'MACD': 'CD001', 'MADX': 'DX001', 'MATX': 'TX001', 'GIA': 2000000, 'HTTTOAN': 'TIEN MAT', 'DIEM': 7.2},
    {'MACD': 'CD002', 'MADX': 'DX002', 'MATX': 'TX002', 'GIA': 4200000, 'HTTTOAN': 'VIETCOMBANK', 'DIEM': 3.5},
    {'MACD': 'CD003', 'MADX': 'DX003', 'MATX': 'TX005', 'GIA': 5500000, 'HTTTOAN': 'VIETCOMBANK', 'DIEM': 9.3},
    {'MACD': 'CD004', 'MADX': 'DX004', 'MATX': 'TX001', 'GIA': 1300000, 'HTTTOAN': 'VIETCOMBANK', 'DIEM': 8.6},
    {'MACD': 'CD005', 'MADX': 'DX005', 'MATX': 'TX002', 'GIA': 4400000, 'HTTTOAN': 'TIEN MAT', 'DIEM': 2.0},
    {'MACD': 'CD006', 'MADX': 'DX006', 'MATX': 'TX005', 'GIA': 4600000, 'HTTTOAN': 'TIEN MAT', 'DIEM': 4.0}
])

# 1
s = text("SELECT CHUYENDI.MACD, CHUYENDI.DIEM FROM CHUYENDI WHERE CHUYENDI.DIEM >= 4.5")
for row in conn.execute(s):
    print(row)
# 2
s = text(
    "SELECT DATXE.MADX, DATXE.DDI, DATXE.DDEN, DATXE.TGDAT FROM DATXE, KH WHERE DATXE.MAKH = KH.MAKH AND KH.HOTEN = "
    "'Nguyen Van A'")
for row in conn.execute(s):
    print(row)

# 3
s = text(
    "SELECT DOIXE.MADX, DOIXE.MATX, TAIXE.HOTEN, TAIXE.SDT, DOIXE.TGBDAU, DOIXE.TGKTHUC, DOIXE.KQUA FROM DOIXE, "
    "TAIXE WHERE TAIXE.MATX = DOIXE.MATX AND DOIXE.MATX = 'TX005' AND DOIXE.KQUA = 'TAI XE HUY'")
for row in conn.execute(s):
    print(row)

# 4
s = text(
    "SELECT KH.MAKH, KH.HOTEN, KH.SDT, COUNT(DATXE.MAKH) AS SLCD FROM KH, DATXE, CHUYENDI WHERE KH.MAKH = DATXE.MAKH "
    "AND DATXE.MADX = CHUYENDI.MADX AND CHUYENDI.GIA > 400000 AND CHUYENDI.HTTTOAN = 'VIETCOMBANK' GROUP BY(KH.MAKH) "
    "ORDER BY SLCD")
for row in conn.execute(s):
    print(row)

# 5
s = text(
    "SELECT KH.MAKH, KH.HOTEN, KH.SDT FROM KH, DATXE, CHUYENDI WHERE KH.MAKH = DATXE.MAKH AND DATXE.MADX = "
    "CHUYENDI.MADX AND CHUYENDI.HTTTOAN = 'VIETCOMBANK' GROUP BY(KH.MAKH)")
for row in conn.execute(s):
    print(row)

# 6
s = text(
    "SELECT KH.MAKH, KH.HOTEN, KH.SDT FROM KH, DATXE, CHUYENDI WHERE KH.MAKH = DATXE.MAKH AND DATXE.MADX = "
    "CHUYENDI.MADX AND CHUYENDI.HTTTOAN = 'VIETCOMBANK' AND CHUYENDI.HTTTOAN = 'TIEN MAT' GROUP BY(KH.MAKH)")
for row in conn.execute(s):
    print(row)
