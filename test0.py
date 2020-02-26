import os 
import itertools
import time
import numpy as np 

dirpath = os.getcwd()
file_name ='c_incunabula.txt'
file_name = 'b_read_on.txt'
books__ = []

def read_file(file_name):
	return [line.rstrip('\n') for line in open(file_name) if len(line) and line[0] != '#']

def get_int(file):
	init = file[0]
	D = init.split(" ")[2]
	L = init.split(" ")[1]
	B = init.split(" ")[0]
	return B,L,D

def books__scores(B, file):
	line1 = file[1].split(" ")
	scores = list(line1)
	book_index = [i for i in range(int(B))]
	book_scores = {ind:score_ for ind,score_ in zip(book_index,scores)}
	return book_scores

def get_lib(file, L):
	i=4
	a = np.array([int(x) for x in file[2].split(" ")])
	while i<len(file) : 
		a = np.vstack((a, np.array([int(x) for x in file[i].split(" ")])))
		i=i+2 
	index = np.array([2])
	for i in range(4,int(L)*2+2,2) : 
		ind = np.array([i])
		index = np.vstack((index,ind))
	a = np.hstack((index,a))
	#index = index.transpose()
	#print(len(a))
	#print(len(index))
	#a = a.sort(axis=2)
	
	#print(index)
	return a
def get_books(file, book_i):
	return file[book_i+1]

def min_temp(x):
	min_ = x[0,2]
	ligne = x[0,0]
	res = x[0]
	y = np.array([[],[]])
	
	for e in x:
		if e[2] <=min_:
			min_ = e[2]
			ligne = e[0]
			res = e
	
	index__ = (ligne/2)-1
	index__ = np.where(x[0,:] == res)
	print(int(index__))	
	print(x.size)
	x = np.delete(x,int(index__),0)
	return res, x


def prend_books(books,nbr_book_prise):

	for b in books : 
		a="s"
	return a

def get_good(file,a , D):
	global books__
	duree_consome= 0 
	days_nbr = int(D)
	libraries_restante = a
	libraries = []
	text = ""
	cpt = 0
	while duree_consome < days_nbr :
		x,libraries_restante = min_temp(libraries_restante)
		#print(x)
		#print(len(libraries_restante))
		duree_signature = x[2]

		duree_consome = duree_consome + duree_signature
		#len(lib)  nbr de bib prise
		libraries.append(int(x[0]/2)-1)

		lib_i = x[0]
		#print(book_i)
		books = get_books(file, lib_i)	

		nb_livre = x[1]
		nb_envoie = x[3]

		div = int(nb_livre/nb_envoie)
		TempMax  = days_nbr - duree_consome
		nbr_book_prise = TempMax if div > TempMax else div
		lib__ = int(x[0]/2)-1
		second_line = str(lib__)+' '+str(nbr_book_prise)
		books = books.split(" ")
		#books_prise= prend_books(books,nbr_book_prise)
		books_prise = books[:nbr_book_prise]
		#get_score(file,books,nbr_book_prise)
		text = text + '\n'+ second_line
		text = text + '\n'+ ' '.join([str(elem) for elem in books_prise]) 
		cpt = cpt +1
		
	text = str(cpt) + '\n'+ text
	#print(text)
		

def main():
	file = read_file(file_name)
	file = file[:len(file)-1]
	B,L,D = get_int(file)
	books_scores = books__scores(B, file)
	a = get_lib(file, L)
	get_good(file, a , D)

main()