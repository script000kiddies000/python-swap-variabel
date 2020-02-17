def balik(awal,akhir):
  swap = awal
  awal = akhir
  akhir = swap
  return awal,akhir

awal = raw_input(" masukkan nama awal\t : ")
akhir = raw_input(" masukkan nama akhir\t : ")

awal , akhir = balik(awal, akhir)

print "=======================\n nama lengkap setelah di balik\n======================= "
print " nama awal\t : ", awal
print " nama akhir\t : ", akhir
