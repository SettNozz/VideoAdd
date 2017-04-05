cimport cmuxing 


cdef class Stream:
    cdef cmuxing.Stream_context* _c_stream 
    def __cinit__(self):
        self._c_stream = cmuxing.muxing_preparation()

    #prototype
    cpdef write_and_decode(self, img):
        spam = cmuxing.muxing_get_frame(self._c_stream)
        
        # need to change format:

        rows, cols = img.shape
        width, height = cols, rows
        for x in range(width):
            for y in range(height):
                spam[0][y*width + x] = <char><long long>(img[y,x] % 255)

        for x in range(width/2):
            for y in range(height/2):
                spam[1][y*(width/2) + x] = 100
                spam[2][y*(width/2) + x] = 100
                
        cmuxing.muxing_write_video_frame(self._c_stream)


    
    def __dealloc__(self):
        cmuxing.muxing_Close_stream(self._c_stream)
