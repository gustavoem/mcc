all: pendulum.c
	gcc -g pendulum.c -I/usr/local/include -L/usr/local/lib -lsundials_cvode -lsundials_nvecserial -lm /usr/lib/x86_64-linux-gnu/librt.so -Wl,-rpath,/usr/local/lib
