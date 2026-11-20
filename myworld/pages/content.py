"""Portfolio projects are intentionally version-controlled in portfolio_data.py."""
from .portfolio_data import PROJECTS


def get_projects():
    """Return copies so templates cannot change the source portfolio content."""
    return [dict(project) for project in PROJECTS]
