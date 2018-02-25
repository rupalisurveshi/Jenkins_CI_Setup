# Python script to create a makefile and compile the source code

import os, sys, argparse

#function to create a makefile
def create_makefile(source_dir, headers_dir, headers_list, source_list=[]):
	obj_list = ' '.join([c.replace('.c', '.o') for c in source_list])
	with open('makefile', 'w') as my_makefile:
		my_makefile.write('HDRDIR =./{}\nCC=gcc\nCFLAGS=-I$(HDRDIR)\n'.format(headers_dir))
		my_makefile.write('OBJDIR={}\n\n_DEPS={}\nDEPS=$(patsubst %,$(HDRDIR)/%,$(_DEPS))\n\n'.format(source_dir, headers_list))
		my_makefile.write('_OBJ={}\nOBJ = $(patsubst %,$(OBJDIR)/%,$(_OBJ))\n\n'.format(obj_list))	
		my_makefile.write('$(OBJDIR)/%.o: %.c $(DEPS)\n\t$(CC) -c -o $@ $< $(CFLAGS)\n\n')
		my_makefile.write('finalmake: $(OBJ)\n\t$(CC) -o $@ $^ $(CFLAGS)\n\n')
		my_makefile.write('.PHONY: clean\n\nclean:\n\trm -f $(OBJDIR)/*.o *~ core $(INCDIR)/*~')
	if os.path.isfile('./makefile'):
		print "INFO: Successfuly created 'makefile'"
		return 0
	else:
		print "INFO: Error in creating 'makefile'"
		return 1

# Main function
def my_main():
	# get current directory
	parser = argparse.ArgumentParser()
	parser.add_argument('source_dir_name', help='source dir name')
	parser.add_argument('headers_dir_name', help='headers dir name')
	args = parser.parse_args()
	cwd = os.getcwd()
	srcdir = cwd + "/" + args.source_dir_name
	hdrdir = cwd + "/" + args.headers_dir_name
	srclist = os.listdir(srcdir)
	headerlist = ' '.join(os.listdir(hdrdir))

	print "\n#####################################################"
	print "#           Script to create makefile               #"
	print "#####################################################\n"
	print "INFO: Current working directory  : ", cwd
	print "INFO: Source code directory      : ", srcdir
	print "INFO: Include headers' directory : ", hdrdir
	print "INFO: Source code to compile     : ", ' '.join(srclist)
	print "INFO: Headers to include         : ", headerlist
	print "\nINFO: Creating 'malkefile' in ", cwd, "\n"
	ret = create_makefile(args.source_dir_name, args.headers_dir_name, headerlist, srclist)
	print "#####################################################\n"
	if ret == 0:
		return 0
	else:
		return 1
if __name__ == '__main__':
	my_main()
