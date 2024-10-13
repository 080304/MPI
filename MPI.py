#ADINNI SALSABILLAH
#225150307111014
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    for i in range(1, size):
        pesan = f"Halo dari proses {rank}"
        comm.send(pesan, dest=i, tag=0)
    print(f"Proses {rank} mengirim pesan ke semua proses lain.")
else:
    pesan = comm.recv(source=0, tag=0)
    print(f"Proses {rank} menerima pesan: {pesan}")