int rangeBitwiseAnd(int l, int r){
       int c=0;
       while(1){
        if(l==r){
            l<<=c;
            break;
        }
        else{
            l>>=1;
            r>>=1;
            c++;
        }
    }
    return l;
}