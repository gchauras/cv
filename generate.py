import sys
import yaml

def latex_cv(in_file, out_file, show_refs):
    """
    Generate XeLaTeX code for CV

    Parameters
    ----------
    in_file: string
             Input YAML file containing cv data
    out_file: string
              Name of output .tex file
    show_refs: bool
               Flag to indicate if list of referees should be written or not
    """
    cv = []
    with open(in_file) as f:
        cv = yaml.safe_load(f)

    with open(out_file, 'w') as f:
        f.write('\include{preamble} \n')
        f.write('\\begin{document} \n')

        f.write('\\begin{center} \n')
        f.write('\headerstyle{' + cv['name'].upper() + '} \\\\ \n')
        affiliation = ''
        if cv['affiliation']:
            affiliation = cv['affiliation'].upper()
        if cv['address']:
            affiliation = cv['address'].upper()
        f.write('\headercontactstyle{' +
                affiliation'] else '' + ', ' +
                cv['address'].upper() if cv['address'] else '' + '\\\\' + '\mail{' +
                cv['email'] + '} \quad \www{' +
                cv['web'] + '}} \n')
        f.write('\\vspace{0.3cm} \n')
        f.write('\end{center} \n')

        f.write('\cvsection{RESEARCH INTERESTS} \n')
        f.write('\\begin{shortcvitems} \n')
        for i in cv['research_interests']:
            f.write('\item ' + i + '\n')
        f.write('\\end{shortcvitems} \n')

        f.write('\cvsection{EXPERIENCE} \n')
        f.write('\\begin{cvitems} \n')
        for p in cv['positions']:
            f.write('\item \position')
            f.write('{' + p['date'] + '} \n')
            f.write('{' + p['title'] + '} \n')
            f.write('{' + p['affiliation'] + '} \n')
            f.write('{' + p['location'] + '} \n')
            if 'mentor' in p and p['mentor'] and p['mentor'] is not None:
                f.write('{' + p['mentor'] + '} \n')
            else:
                f.write('{} \n')
            if 'notes' in p and p['notes'] and p['notes'] is not None:
                f.write('{' + p['notes'] + '} \n')
            else:
                f.write('{} \n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{EDUCATION} \n')
        f.write('\\begin{cvitems} \n')
        for p in cv['education']:
            f.write('\item \position')
            f.write('{' + p['date'] + '} \n')
            f.write('{' + p['title'] + '} \n')
            f.write('{' + p['affiliation'] + '} \n')
            f.write('{' + p['location'] + '} \n')
            if 'mentor' in p and p['mentor'] and p['mentor'] is not None:
                f.write('{' + p['mentor'] + '} \n')
            else:
                f.write('{} \n')
            if 'thesis' in p and p['thesis'] and p['thesis'] is not None:
                f.write('{' + p['thesis'] + '} \n')
            else:
                f.write('{} \n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{VISITING POSITIONS} \n')
        f.write('\\begin{cvitems} \n')
        for p in cv['visiting_positions']:
            f.write('\item \position')
            f.write('{' + p['date'] + '} \n')
            f.write('{' + p['title'] + '} \n')
            f.write('{' + p['affiliation'] + '} \n')
            f.write('{' + p['location'] + '} \n')
            if 'mentor' in p and p['mentor'] and p['mentor'] is not None:
                f.write('{' + p['mentor'] + '} \n')
            else:
                f.write('{} \n')
            if 'notes' in p and p['notes'] and p['notes'] is not None:
                f.write('{' + p['notes'] + '} \n')
            else:
                f.write('{} \n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{PUBLICATIONS} \n')
        f.write('\\begin{cvitems} \n')
        prev_year = 0
        for p in cv['publications']:
            f.write('\item \publication')
            if prev_year != p['year']:
                f.write('{' + str(p['year']) + '}')
                prev_year = p['year']
            else:
                f.write('{}')
            f.write('{' + p['author']  + '}')
            f.write('{' + p['title']   + '}')
            if 'note' in p and p['note']:
                f.write('{' + p['journal'] + ' (' +  p['note'] + ')' + '}')
            else:
                f.write('{' + p['journal'] + '}')
            f.write('{' + p['url']     + '}')
            f.write('{' + p['doi']     + '}\n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{SUPERVISED THESES} \n')
        f.write('\\begin{cvitems} \n')
        for p in cv['supervised_theses']:
            f.write('\item \publication')
            f.write('{' + p['date']   + '}')
            f.write('{' + p['author'] + '}')
            f.write('{' + p['title']  + '}')
            f.write('{' + p['school'] + '}')
            f.write('{}')
            f.write('{}\n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{TEACHING} \n')
        f.write('\\begin{shortcvitems} \n')
        for t in cv['teaching']:
            f.write('\item \\notes{' + t['date'] + '}' + t['title'] +
                    ' \href{' + t['url'] + '}{' + t['number'] + '}'
                    ' \dotfill ' + t['school'] + '\n')
        f.write('\\end{shortcvitems} \n')

        f.write('\cvsection{PROFESSIONAL ACTIVITIES} \n')
        f.write('\\begin{cvitems} \n')
        f.write('\item \\notes{Journal reviews} \n')
        for r in cv['reviews']['journal']:
            years = [ str(y['year']) for y in r['years'] ]
            f.write('\jreview' +
                    '{' + ', '.join(years) + '}'
                    '{' + r['title']       + '}' +
                    '{' + r['url']         + '} \\\\ \n')

        f.write('\item \\notes{Conference reviews} \n')
        for r in cv['reviews']['conference']:
            years = [ str(y['year']) for y in r['years'] ]
            f.write('\creview' +
                    '{' + ', '.join(years) + '}' +
                    '{' + r['title']       + '} \\\\ \n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{SCHOLARSHIPS AND AWARDS} \n')
        f.write('\\begin{shortcvitems} \n')
        for s in cv['awards']:
            f.write('\item \\notes{' + s['date'] + '}' + s['detail'] + '\n')
        f.write('\\end{shortcvitems} \n')

        f.write('\cvsection{TECHNICAL SKILLS} \n')
        f.write('\\begin{cvitems} \n')
        f.write('\item ' + ', '.join(cv['technical_skills']) + '\n')
        f.write('\\end{cvitems} \n')

        f.write('\cvsection{REFERENCES} \n')
        if show_refs:
            f.write('\\begin{cvitems} \n')
            for s in cv['references']:
                f.write('\item '  + s['name'] + ' \\\\ \n' +
                        '{ \itshape ' + s['title'] + '} \\\\ \n'
                        '\www{'   + s['www'] + '} \quad'
                        '\mail{' + s['mail'] + '} \n')
            f.write('\\end{cvitems} \n')
        else:
            f.write('Available on request \n')
        f.write('\end{document}')

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv)==4:
        in_file   = sys.argv[1]
        out_file  = sys.argv[2]
        show_refs = True if int(sys.argv[3])>0 else False
        latex_cv(in_file, out_file, show_refs)
        sys.exit(0)
    else:
        print('\n\nUsage: generate.py [in_file] [out_file] [show_refs]\n' +
              latex_cv.__doc__)
        sys.exit(-1)
