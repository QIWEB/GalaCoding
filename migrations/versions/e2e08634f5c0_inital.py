"""inital

Revision ID: e2e08634f5c0
Revises: None
Create Date: 2016-05-09 22:53:17.260000

"""

# revision identifiers, used by Alembic.
revision = 'e2e08634f5c0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=True)
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10), nullable=True),
    sa.Column('refer_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_id'), 'tags', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=64), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('avatar_url', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_avatar_url'), 'users', ['avatar_url'], unique=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.create_index(op.f('ix_follows_followed_id'), 'follows', ['followed_id'], unique=False)
    op.create_index(op.f('ix_follows_follower_id'), 'follows', ['follower_id'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('viewed_count', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_author_id'), 'posts', ['author_id'], unique=False)
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('agree_count', sa.Integer(), nullable=True),
    sa.Column('disagree_count', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_author_id'), 'comments', ['author_id'], unique=False)
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    op.create_index(op.f('ix_comments_post_id'), 'comments', ['post_id'], unique=False)
    op.create_table('concern_posts',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.create_index(op.f('ix_concern_posts_post_id'), 'concern_posts', ['post_id'], unique=False)
    op.create_index(op.f('ix_concern_posts_user_id'), 'concern_posts', ['user_id'], unique=False)
    op.create_table('posttags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posttags_id'), 'posttags', ['id'], unique=False)
    op.create_index(op.f('ix_posttags_post_id'), 'posttags', ['post_id'], unique=False)
    op.create_index(op.f('ix_posttags_tag_id'), 'posttags', ['tag_id'], unique=False)
    op.create_table('remarkposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('attitude', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_remarkposts_owner_id'), 'remarkposts', ['owner_id'], unique=False)
    op.create_index(op.f('ix_remarkposts_post_id'), 'remarkposts', ['post_id'], unique=False)
    op.create_table('remarks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('attitude', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_remarks_comment_id'), 'remarks', ['comment_id'], unique=False)
    op.create_index(op.f('ix_remarks_owner_id'), 'remarks', ['owner_id'], unique=False)
    op.create_table('subcomment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('for_comment_id', sa.Integer(), nullable=True),
    sa.Column('from_comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['for_comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['from_comment_id'], ['comments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subcomment_for_comment_id'), 'subcomment', ['for_comment_id'], unique=False)
    op.create_index(op.f('ix_subcomment_from_comment_id'), 'subcomment', ['from_comment_id'], unique=False)
    op.create_index(op.f('ix_subcomment_id'), 'subcomment', ['id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subcomment_id'), table_name='subcomment')
    op.drop_index(op.f('ix_subcomment_from_comment_id'), table_name='subcomment')
    op.drop_index(op.f('ix_subcomment_for_comment_id'), table_name='subcomment')
    op.drop_table('subcomment')
    op.drop_index(op.f('ix_remarks_owner_id'), table_name='remarks')
    op.drop_index(op.f('ix_remarks_comment_id'), table_name='remarks')
    op.drop_table('remarks')
    op.drop_index(op.f('ix_remarkposts_post_id'), table_name='remarkposts')
    op.drop_index(op.f('ix_remarkposts_owner_id'), table_name='remarkposts')
    op.drop_table('remarkposts')
    op.drop_index(op.f('ix_posttags_tag_id'), table_name='posttags')
    op.drop_index(op.f('ix_posttags_post_id'), table_name='posttags')
    op.drop_index(op.f('ix_posttags_id'), table_name='posttags')
    op.drop_table('posttags')
    op.drop_index(op.f('ix_concern_posts_user_id'), table_name='concern_posts')
    op.drop_index(op.f('ix_concern_posts_post_id'), table_name='concern_posts')
    op.drop_table('concern_posts')
    op.drop_index(op.f('ix_comments_post_id'), table_name='comments')
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_index(op.f('ix_comments_author_id'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_index(op.f('ix_posts_author_id'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_follows_follower_id'), table_name='follows')
    op.drop_index(op.f('ix_follows_followed_id'), table_name='follows')
    op.drop_table('follows')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_avatar_url'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tags_id'), table_name='tags')
    op.drop_table('tags')
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    ### end Alembic commands ###
