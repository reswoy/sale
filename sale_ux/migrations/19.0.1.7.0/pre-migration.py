from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """
    Remove stale DB views referencing use_search_filter_amount.
    This field was removed from res.config.settings in v19.
    Any view still referencing it from 18.0 must be cleaned up
    before sale_ux loads its updated view definitions.
    """
    if not version:
        return
    env.cr.execute("""
        DELETE FROM ir_ui_view
        WHERE arch_db::text LIKE '%use_search_filter_amount%'
    """)
