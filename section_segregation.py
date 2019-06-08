import pandas as pd
from flask import Flask,render_template,request
csv_test=Flask(__name__)

@csv_test.route("/")
def main():
    return render_template('hello.html')
@csv_test.route("/segregate",methods=["post"])
def segregate():
    user = request.form['userid']
    pas = request.form['password']
    if user == pas == 'admin':
        if request.form['submit']:
            return render_template('hello1.html')

@csv_test.route("/segregate1", methods=["post"])
def segregate1():
            if request.form['gen_sec']:
                count = 0
                count1 = 0
                data = pd.read_csv('C:\\Users\\SSN\\Desktop\\test_py.csv')
                df = pd.DataFrame(data)
                gb = df.groupby('Department')
                ece = gb.get_group('ECE')
                cse = gb.get_group('CSE')
                eee = gb.get_group('EEE')
                it = gb.get_group('IT')
                mech = gb.get_group('Mech')
                bme = gb.get_group('BME')
                civil = gb.get_group('Civil')
                chemical = gb.get_group('Chemical')

                for x in range(1, 9):

                    sel_ece = ece.sample(9, random_state=x)
                    ece = pd.concat([ece, sel_ece])
                    ece = ece.drop_duplicates(keep=False)

                    sel_cse = cse.sample(9, random_state=x)
                    cse = pd.concat([cse, sel_cse])
                    cse = cse.drop_duplicates(keep=False)

                    sel_eee = eee.sample(9, random_state=x)
                    eee = pd.concat([eee, sel_eee])
                    eee = eee.drop_duplicates(keep=False)

                    sel_it = it.sample(9, random_state=x)
                    it = pd.concat([it, sel_it])
                    it = it.drop_duplicates(keep=False)

                    sel_mech = mech.sample(9, random_state=x)
                    mech = pd.concat([mech, sel_mech])
                    mech = mech.drop_duplicates(keep=False)

                    sel_bme = bme.sample(5, random_state=x)
                    bme = pd.concat([bme, sel_bme])
                    bme = bme.drop_duplicates(keep=False)

                    sel_chemical = chemical.sample(5, random_state=x)
                    chemical = pd.concat([chemical, sel_chemical])
                    chemical = chemical.drop_duplicates(keep=False)

                    sel_civil = civil.sample(5, random_state=x)
                    civil = pd.concat([civil, sel_civil])
                    civil = civil.drop_duplicates(keep=False)

                    if count == 0:
                        section_A = sel_ece
                        section_A = pd.concat([section_A, sel_cse])
                        section_A = pd.concat([section_A, sel_eee])
                        section_A = pd.concat([section_A, sel_it])
                        section_A = pd.concat([section_A, sel_mech])
                        section_A = pd.concat([section_A, sel_bme])
                        section_A = pd.concat([section_A, sel_chemical])
                        section_A = pd.concat([section_A, sel_civil])
                        count = count + 1
                        tot_A = 60
                        # section_A.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_A.csv', index=False)
                    elif count == 1:
                        section_B = sel_ece
                        section_B = pd.concat([section_B, sel_cse])
                        section_B = pd.concat([section_B, sel_eee])
                        section_B = pd.concat([section_B, sel_it])
                        section_B = pd.concat([section_B, sel_mech])
                        section_B = pd.concat([section_B, sel_bme])
                        section_B = pd.concat([section_B, sel_chemical])
                        section_B = pd.concat([section_B, sel_civil])
                        count = count + 1
                        tot_B = 60
                        # section_B.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_B.csv', index=False)
                    elif count == 2:
                        section_C = sel_ece
                        section_C = pd.concat([section_C, sel_cse])
                        section_C = pd.concat([section_C, sel_eee])
                        section_C = pd.concat([section_C, sel_it])
                        section_C = pd.concat([section_C, sel_mech])
                        section_C = pd.concat([section_C, sel_bme])
                        section_C = pd.concat([section_C, sel_chemical])
                        section_C = pd.concat([section_C, sel_civil])
                        count = count + 1
                        tot_C = 60
                        # section_C.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_C.csv', index=False)
                    elif count == 3:
                        section_D = sel_ece
                        section_D = pd.concat([section_D, sel_cse])
                        section_D = pd.concat([section_D, sel_eee])
                        section_D = pd.concat([section_D, sel_it])
                        section_D = pd.concat([section_D, sel_mech])
                        section_D = pd.concat([section_D, sel_bme])
                        section_D = pd.concat([section_D, sel_chemical])
                        section_D = pd.concat([section_D, sel_civil])
                        count = count + 1
                        tot_D = 60
                        # section_D.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_D.csv', index=False)
                    elif count == 4:
                        section_E = sel_ece
                        section_E = pd.concat([section_E, sel_cse])
                        section_E = pd.concat([section_E, sel_eee])
                        section_E = pd.concat([section_E, sel_it])
                        section_E = pd.concat([section_E, sel_mech])
                        section_E = pd.concat([section_E, sel_bme])
                        section_E = pd.concat([section_E, sel_chemical])
                        section_E = pd.concat([section_E, sel_civil])
                        count = count + 1
                        tot_E = 60
                        # section_E.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_E.csv', index=False)
                    elif count == 5:
                        section_F = sel_ece
                        section_F = pd.concat([section_F, sel_cse])
                        section_F = pd.concat([section_F, sel_eee])
                        section_F = pd.concat([section_F, sel_it])
                        section_F = pd.concat([section_F, sel_mech])
                        section_F = pd.concat([section_F, sel_bme])
                        section_F = pd.concat([section_F, sel_chemical])
                        section_F = pd.concat([section_F, sel_civil])
                        count = count + 1
                        tot_F = 60
                        # section_F.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_F.csv', index=False)
                    elif count == 6:
                        section_G = sel_ece
                        section_G = pd.concat([section_G, sel_cse])
                        section_G = pd.concat([section_G, sel_eee])
                        section_G = pd.concat([section_G, sel_it])
                        section_G = pd.concat([section_G, sel_mech])
                        section_G = pd.concat([section_G, sel_bme])
                        section_G = pd.concat([section_G, sel_chemical])
                        section_G = pd.concat([section_G, sel_civil])
                        count = count + 1
                        tot_G = 60
                        # section_G.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_G.csv', index=False)
                    elif count == 7:
                        section_H = sel_ece
                        section_H = pd.concat([section_H, sel_cse])
                        section_H = pd.concat([section_H, sel_eee])
                        section_H = pd.concat([section_H, sel_it])
                        section_H = pd.concat([section_H, sel_mech])
                        section_H = pd.concat([section_H, sel_bme])
                        section_H = pd.concat([section_H, sel_chemical])
                        section_H = pd.concat([section_H, sel_civil])
                        count = count + 1
                        tot_H = 60
                        # section_H.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_H.csv', index=False)
                if count == 8:
                    sel_ece = ece.sample(9, random_state=9)
                    ece = pd.concat([ece, sel_ece])
                    ece = ece.drop_duplicates(keep=False)

                    sel_cse = cse.sample(9, random_state=9)
                    cse = pd.concat([cse, sel_cse])
                    cse = cse.drop_duplicates(keep=False)

                    sel_eee = eee.sample(10, random_state=9)
                    eee = pd.concat([eee, sel_eee])
                    eee = eee.drop_duplicates(keep=False)

                    sel_it = it.sample(10, random_state=9)
                    it = pd.concat([it, sel_it])
                    it = it.drop_duplicates(keep=False)

                    sel_mech = mech.sample(10, random_state=9)
                    mech = pd.concat([mech, sel_mech])
                    mech = mech.drop_duplicates(keep=False)

                    sel_bme = bme.sample(4, random_state=9)
                    bme = pd.concat([bme, sel_bme])
                    bme = bme.drop_duplicates(keep=False)

                    sel_chemical = chemical.sample(4, random_state=9)
                    chemical = pd.concat([chemical, sel_chemical])
                    chemical = chemical.drop_duplicates(keep=False)

                    sel_civil = civil.sample(4, random_state=9)
                    civil = pd.concat([civil, sel_civil])
                    civil = civil.drop_duplicates(keep=False)

                    section_I = sel_ece
                    section_I = pd.concat([section_I, sel_cse])
                    section_I = pd.concat([section_I, sel_eee])
                    section_I = pd.concat([section_I, sel_it])
                    section_I = pd.concat([section_I, sel_mech])
                    section_I = pd.concat([section_I, sel_bme])
                    section_I = pd.concat([section_I, sel_chemical])
                    section_I = pd.concat([section_I, sel_civil])
                    count = count + 1
                    tot_I = 60
                    # section_I.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_I.csv', index=False)

                if count == 9:
                    sel_ece = ece.sample(9, random_state=10)
                    ece = pd.concat([ece, sel_ece])
                    ece = ece.drop_duplicates(keep=False)

                    sel_cse = cse.sample(10, random_state=10)
                    cse = pd.concat([cse, sel_cse])
                    cse = cse.drop_duplicates(keep=False)

                    sel_eee = eee.sample(9, random_state=10)
                    eee = pd.concat([eee, sel_eee])
                    eee = eee.drop_duplicates(keep=False)

                    sel_it = it.sample(10, random_state=10)
                    it = pd.concat([it, sel_it])
                    it = it.drop_duplicates(keep=False)

                    sel_mech = mech.sample(10, random_state=10)
                    mech = pd.concat([mech, sel_mech])
                    mech = mech.drop_duplicates(keep=False)

                    sel_bme = bme.sample(4, random_state=10)
                    bme = pd.concat([bme, sel_bme])
                    bme = bme.drop_duplicates(keep=False)

                    sel_chemical = chemical.sample(4, random_state=10)
                    chemical = pd.concat([chemical, sel_chemical])
                    chemical = chemical.drop_duplicates(keep=False)

                    sel_civil = civil.sample(4, random_state=10)
                    civil = pd.concat([civil, sel_civil])
                    civil = civil.drop_duplicates(keep=False)

                    section_J = sel_ece
                    section_J = pd.concat([section_J, sel_cse])
                    section_J = pd.concat([section_J, sel_eee])
                    section_J = pd.concat([section_J, sel_it])
                    section_J = pd.concat([section_J, sel_mech])
                    section_J = pd.concat([section_J, sel_bme])
                    section_J = pd.concat([section_J, sel_chemical])
                    section_J = pd.concat([section_J, sel_civil])
                    count = count + 1
                    tot_J = 60
                    # section_J.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_J.csv', index=False)

                if count == 10:
                    sel_ece = ece.sample(10, random_state=11)
                    ece = pd.concat([ece, sel_ece])
                    ece = ece.drop_duplicates(keep=False)

                    sel_cse = cse.sample(9, random_state=11)
                    cse = pd.concat([cse, sel_cse])
                    cse = cse.drop_duplicates(keep=False)

                    sel_eee = eee.sample(9, random_state=11)
                    eee = pd.concat([eee, sel_eee])
                    eee = eee.drop_duplicates(keep=False)

                    sel_it = it.sample(10, random_state=11)
                    it = pd.concat([it, sel_it])
                    it = it.drop_duplicates(keep=False)

                    sel_mech = mech.sample(10, random_state=11)
                    mech = pd.concat([mech, sel_mech])
                    mech = mech.drop_duplicates(keep=False)

                    sel_bme = bme.sample(4, random_state=11)
                    bme = pd.concat([bme, sel_bme])
                    bme = bme.drop_duplicates(keep=False)

                    sel_chemical = chemical.sample(4, random_state=11)
                    chemical = pd.concat([chemical, sel_chemical])
                    chemical = chemical.drop_duplicates(keep=False)

                    sel_civil = civil.sample(4, random_state=11)
                    civil = pd.concat([civil, sel_civil])
                    civil = civil.drop_duplicates(keep=False)

                    section_K = sel_ece
                    section_K = pd.concat([section_K, sel_cse])
                    section_K = pd.concat([section_K, sel_eee])
                    section_K = pd.concat([section_K, sel_it])
                    section_K = pd.concat([section_K, sel_mech])
                    section_K = pd.concat([section_K, sel_bme])
                    section_K = pd.concat([section_K, sel_chemical])
                    section_K = pd.concat([section_K, sel_civil])
                    count = count + 1
                    tot_K = 60
                    # section_K.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_K.csv', index=False)

                if count == 11:
                    sel_ece = ece.sample(10, random_state=12)
                    ece = pd.concat([ece, sel_ece])
                    ece = ece.drop_duplicates(keep=False)

                    sel_cse = cse.sample(10, random_state=12)
                    cse = pd.concat([cse, sel_cse])
                    cse = cse.drop_duplicates(keep=False)

                    sel_eee = eee.sample(10, random_state=12)
                    eee = pd.concat([eee, sel_eee])
                    eee = eee.drop_duplicates(keep=False)

                    sel_it = it.sample(9, random_state=12)
                    it = pd.concat([it, sel_it])
                    it = it.drop_duplicates(keep=False)

                    sel_mech = mech.sample(9, random_state=12)
                    mech = pd.concat([mech, sel_mech])
                    mech = mech.drop_duplicates(keep=False)

                    sel_bme = bme.sample(4, random_state=12)
                    bme = pd.concat([bme, sel_bme])
                    bme = bme.drop_duplicates(keep=False)

                    sel_chemical = chemical.sample(4, random_state=12)
                    chemical = pd.concat([chemical, sel_chemical])
                    chemical = chemical.drop_duplicates(keep=False)

                    sel_civil = civil.sample(4, random_state=12)
                    civil = pd.concat([civil, sel_civil])
                    civil = civil.drop_duplicates(keep=False)

                    section_L = sel_ece
                    section_L = pd.concat([section_L, sel_cse])
                    section_L = pd.concat([section_L, sel_eee])
                    section_L = pd.concat([section_L, sel_it])
                    section_L = pd.concat([section_L, sel_mech])
                    section_L = pd.concat([section_L, sel_bme])
                    section_L = pd.concat([section_L, sel_chemical])
                    section_L = pd.concat([section_L, sel_civil])
                    count = count + 1
                    tot_L = 60
                    # section_L.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_L.csv', index=False)

                if count == 12:
                    sel_ece = ece.sample(10, random_state=13)
                    ece = pd.concat([ece, sel_ece])
                    ece = ece.drop_duplicates(keep=False)

                    sel_cse = cse.sample(10, random_state=13)
                    cse = pd.concat([cse, sel_cse])
                    cse = cse.drop_duplicates(keep=False)

                    sel_eee = eee.sample(10, random_state=13)
                    eee = pd.concat([eee, sel_eee])
                    eee = eee.drop_duplicates(keep=False)

                    sel_it = it.sample(9, random_state=13)
                    it = pd.concat([it, sel_it])
                    it = it.drop_duplicates(keep=False)

                    sel_mech = mech.sample(9, random_state=13)
                    mech = pd.concat([mech, sel_mech])
                    mech = mech.drop_duplicates(keep=False)

                    sel_bme = bme.sample(4, random_state=13)
                    bme = pd.concat([bme, sel_bme])
                    bme = bme.drop_duplicates(keep=False)

                    sel_chemical = chemical.sample(4, random_state=13)
                    chemical = pd.concat([chemical, sel_chemical])
                    chemical = chemical.drop_duplicates(keep=False)

                    sel_civil = civil.sample(4, random_state=13)
                    civil = pd.concat([civil, sel_civil])
                    civil = civil.drop_duplicates(keep=False)

                    section_M = sel_ece
                    section_M = pd.concat([section_M, sel_cse])
                    section_M = pd.concat([section_M, sel_eee])
                    section_M = pd.concat([section_M, sel_it])
                    section_M = pd.concat([section_M, sel_mech])
                    section_M = pd.concat([section_M, sel_bme])
                    section_M = pd.concat([section_M, sel_chemical])
                    section_M = pd.concat([section_M, sel_civil])
                    count = count + 1
                    tot_M = 60
                    # section_M.to_csv('C:\\Users\\SSN\\Desktop\\Classes\\Section_M.csv', index=False)
                    return render_template('generated.html')
if __name__=="__main__":
    csv_test.run()
