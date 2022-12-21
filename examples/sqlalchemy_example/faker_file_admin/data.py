def build_sample_db(db):
    """Populate a small db with some example entries."""

    db.drop_all()
    db.create_all()
    db.session.commit()
    return
