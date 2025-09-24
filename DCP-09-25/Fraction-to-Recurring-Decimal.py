class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        def repeating_ans(n,d):
            s="";
            di={};
            r=n%d;
            while(r!=0 and r not in di):
                di[r]=len(s);
                r=r*10;
                q=r//d;
                s+=str(q);
                r=r%d;
            if r==0:
                return s;
            else:
                return s[:di[r]]+"("+s[di[r]:]+")";
        ans="";
        n_n=abs(n);
        d_n=abs(d);
        sub_ans=(n_n//d_n);
        if n_n%d_n==0:
            ans+=str(sub_ans);
            if n<0 and d<0 or n>0 and d>0 or n==0:
                return ans;
            else:
                return "-"+ans;
        else:
            ans+=str(sub_ans);
            ans+=".";
            ans+=repeating_ans(n_n,d_n);
            if n<0 and d<0 or n>0 and d>0 or n==0:
                return ans;
            else:
                return "-"+ans;