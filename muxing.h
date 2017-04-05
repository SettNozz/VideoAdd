typedef struct _OutputStream OutputStream;
typedef struct _Stream_context Stream_context;
Stream_context *muxing_preparation(void);
void muxing_Close_stream(Stream_context *);
char** muxing_get_frame(Stream_context *);
int muxing_write_video_frame(Stream_context *);
