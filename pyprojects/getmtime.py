def open(self):
        """
        Setup the internal structure.
        
        NB : Call this function before 
        extracting data from a file.
        """
        if self.file :
            self.file.close()
        try :
            self.file = open(self.path, 'rb')
        except Exception as e:
            raise Exception("python couldn't open file %s : %s" % (self.path, e))
        self.file_size = path.getsize(self.file.name)
        self.creation_date = datetime.fromtimestamp(path.getctime(self.file.name))
        self.modification_date = datetime.fromtimestamp(path.getmtime(self.file.name))
        self.nomenclature = self.get_nomenclature()
        self.factory = self.get_factory()
        self.layout = self.create_layout()






def get_source(self, environment, template):
        pieces = split_template_path(template)
        for searchpath in self.searchpath:
            filename = path.join(searchpath, *pieces)
            f = open_if_exists(filename)
            if f is None:
                continue
            try:
                contents = f.read().decode(self.encoding)
            finally:
                f.close()

            mtime = path.getmtime(filename)

            def uptodate():
                try:
                    return path.getmtime(filename) == mtime
                except OSError:
                    return False
            return contents, filename, uptodate
        raise TemplateNotFound(template) 
