cimport cmuxing 

cdef class Stream:
    cdef cmuxing.Stream_context* _c_stream 
    def __cinit__(self):
        self._c_stream = cmuxing.muxing_preparation()

    #prototype
    cpdef write_and_decode(self, img):
        spam = cmuxing.get_frame(self._c_stream)
        
        # need to change format:

        i_img = 1092
        j_img = 614
        for i in range(i_img):
            for j in range(j_img):
                spam[i*i_img + j] = img[i, j]
        cmuxing.muxing_write_video_frame(self._c_stream)


    
    def __dealloc__(self):
        cmuxing.muxing_Close_stream(self._c_stream)