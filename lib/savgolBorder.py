
# def savgolBorder(a_n, z, ra, ra, theta, h, w, a_out):
#     ra = max(1.5, ra)
#     rb = max(1.5, rb)
#     ira2 = 1 / pow(ra, 2)
#     irb2 = 1 / pow(rb, 2)
#     wr = () (max(ra, rb))
#     s= sin(theta)
#     cost = cos(theta)
#     d0, d1, d2, d3, d4, v0, v1, v2
#     xi, yi, x, y, cpi
#     di, ei, zi, di2, detA, invA, param
#     eps = exp(-300)
    
#     for cp in range(0, w*h):
#         y = cp%h x=cp/h
#         if ((x>=wr) and (x<(w-wr)) and (y>=wr) and (y<(h-wr))):
#             a_out[cp] = a_in[cp]
        
#         else:
            
#             d0=0 d1=0 d2=0 d3=0 d4=0
#             v0=0 v1=0 v2=0
#             for ( u in range(-wr, wr++)):
#                 xi = x + u
#                 if ((xi<0) or (xi>=w)):
#                     continue
#                 for ( v = -wr v <= wr v++ ):
#                     yi = y + v
#                     if ((yi<0) or (yi>=h)):
#                         continue
#                     di = -u*s+ v*cost
#                     ei = u*cost + v*s
#                     if ( (di*di*ira2 + ei*ei*irb2) > 1):
#                         continue
#                     cpi = yi+xi*h
#                     zi = z[cpi]
#                     di2 = di*di
#                     d0 = d0 + 1
#                     d1 = d1 + di
#                     d2 = d2 + di2
#                     d3 = d3 + di*di2
#                     d4 = d4 + di2*di2
#                     v0 = v0 + zi
#                     v1 = v1 + zi*di
#                     v2 = v2 + zi*di2
                
            
            
#             detA = -d2*d2*d2 + 2*d1*d2*d3 - d0*d3*d3 - d1*d1*d4 + d0*d2*d4
#             if (detA>eps):
#                 a_out[cp] = ((-d3*d3+d2*d4)*v0 + (d2*d3-d1*d4)*v1 + (-d2*d2+d1*d3)*v2)/ detA
            
        
    
