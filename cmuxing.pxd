
cdef extern from "muxing.h":
    ctypedef struct OutputStream:
        pass
    ctypedef struct Stream_context:
        pass
    Stream_context* muxing_preparation()
    void muxing_Close_stream(Stream_context *)
    int muxing_write_video_frame(Stream_context *)
    char** get_frame(Stream_context*)
