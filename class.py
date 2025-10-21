#python 3.7.1

class Sekolah :
    pass

sekolah1 = Sekolah()
sekolah2 = Sekolah ()

print(type(sekolah1))
print(type(sekolah2))

class Siswa :
    pass
    
siswa1 = Siswa()
siswa2 = Siswa()

print(type(siswa1))
print(type(siswa2))

sekolah1 = Sekolah()
sekolah1.nama ="SMK PGRI 35 Solokan jeruk"
sekolah1.alamat ="JL RHO Kosasih No 90 Cibodas "
sekolah2 = Sekolah()
sekolah2.nama ="SMKN 9 Bandung "
sekolah2.alamat ="JL Sekarno-Hatta No 10"

print(sekolah1.nama)
print(sekolah1.alamat)
print(sekolah2.nama)
print(sekolah2.alamat)

