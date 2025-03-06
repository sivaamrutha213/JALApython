class RandomAccessFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'rb')
        self.position = 0

    def read(self, size=-1):
        data = b''
        if size == -1:
            while True:
                byte = self.file.read(1)
                if not byte:
                    break
                data += byte
        else:
            for _ in range(size):
                byte = self.file.read(1)
                if not byte:
                    break
                data += byte
        self.position += len(data)
        return data

    def seek(self, offset, whence=0):
        if whence == 0:  # from the start of the file
            self.file.seek(0)
            self.position = 0
        elif whence == 1:  # from the current position
            pass
        elif whence == 2:  # from the end of the file
            self.file.seek(0, 2)
            self.position = self.file.tell()

        while offset > 0:
            self.read(1)
            offset -= 1
        self.position += offset

    def tell(self):
        return self.position

    def close(self):
        self.file.close()


# Example usage:
file_path = 'example.txt'
raf = RandomAccessFile(file_path)

# Read the first 10 bytes
print(raf.read(10))

# Seek to the beginning
raf.seek(0)

# Read the next 10 bytes
print(raf.read(10))

# Get the current position
print(raf.tell())

# Close the file
raf.close()
