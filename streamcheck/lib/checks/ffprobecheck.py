from streamcheck.lib.ffprobe import FFProbe

class FFProbeCheck():
    def __init__(self, stream, timeout):
        self.stream = stream
        self.timeout = timeout 
        #print(self.stream.stream_url)

    def run(self):
        if (self.stream.status != 'OK'):
            metadata=FFProbe(self.stream.stream_url, self.timeout)
            for probe_stream in metadata.streams:
                if probe_stream.is_video():
                    #print('Stream contains {} frames.'.format(probe_stream.frames()))
                    self.stream.status = 'OK'
    
    def run_new(self):
        if (self.stream.new_stream_url and self.stream.status != 'OK'):
            metadata=FFProbe(self.stream.new_stream_url, self.timeout)
            for probe_stream in metadata.streams:
                if probe_stream.is_video():
                    #print('Stream contains {} frames.'.format(probe_stream.frames()))
                    self.stream.status = 'OK'                