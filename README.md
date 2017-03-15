# VideoAdd
This programm read video stream from server, and add any picture, what you want.

To start muxing.c:

New comand:

```{r, engine='bash'}
$ gcc -L/usr/lib/x86_64-linux-gnu -L. -lmuxing_g muxing_py.c -shared -o muxing_py.so  -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7 -fPIC -lavdevice -lavfilter -lavformat -lavcodec -lswresample -lswscale -lavutil -ldl -ldl  -lm -llzma -lz -pthread -g -L/usr/lib/x86_64-linux-gnu -lswresample-ffmpeg -lm -lavutil-ffmpeg -L/usr/lib/x86_64-linux-gnu
```


```{r, engine='bash'}
$ gcc -Llibavcodec -Llibavdevice -Llibavfilter -Llibavformat -Llibavresample -Llibavutil -Llibpostproc -Llibswscale -Llibswresample -Wl,--as-needed -Wl,-z,noexecstack -Wl,--warn-common -Wl,-rpath-link=libpostproc:libswresample:libswscale:libavfilter:libavdevice:libavformat:libavcodec:libavutil:libavresample   -o doc/examples/muxing_g  doc/examples/muxing.c   -lavdevice -lavfilter -lavformat -lavcodec -lswresample -lswscale -lavutil -ldl -ldl -lxcb -lxcb-shm -lxcb -lxcb-xfixes -lxcb-render -lxcb-shape -lxcb -lxcb-shape -lxcb -lX11 -lasound -lm -llzma -lz -pthread -g -Wno-deprecated-declarations -Werror"
```


