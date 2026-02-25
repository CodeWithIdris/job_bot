def generate_cover_letter(job):
    return f"""
Dear Hiring Manager,

I am applying for the {job.get('position')} role at {job.get('company')}.

With strong experience in research strategy, data analysis, and structured reporting,
I have led analytical initiatives that produced measurable insights for decision-makers.

I am particularly drawn to your work in {job.get('tags')}.

I would welcome the opportunity to contribute meaningfully to your team.

Best regards,
Idris Aderoju
"""
