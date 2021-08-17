addpath '/home/3S-LAB/mteil/Documents/octave_packages/iso2mesh'
cd '/home/3S-LAB/mteil/Documents/These/grains_libraries/1MPa/0004/Mesh_files/'
load label_0016.mat
[no, el, reg, hol] = v2s(mat, [1], 1.05, 'cgalmesh') ;
[no1, el1] = meshcheckrepair(no,el,'dup','isolated','deep','meshfix','intersect') ;
[no2, el2] = meshresample(no1,el1,0.9) ;
no3 = smoothsurf(no2,[],meshconn(el2,size(no2)(1))(:,1),3,0.7,'lowpass') ;
[no4, el4] = surfreorient(no3, el2) ;
[node, elem, face] = s2m(no4, el4, keepratio=0.5, maxvol=1.5, method='tetgen') ;
save -v7 grain_0016.mat node elem face