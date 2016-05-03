function [Liste]=generateur_un(b,x,a,n)
	Liste = list(); //Creation de liste
	X = x;
	U = X/n; //Calcul de U0
	Liste($+1) = U; //U0 tete de liste
	for i=1:(n-1)
		y=a*X+b;  //Calcul Xn suivant l'expression
        X=modulo(y,n);  //Enonce
        U=X/n;  //Calcul Un
        Liste($+1) = U; //Ajout Un dans liste
        i=i+1;
    end
endfunction
