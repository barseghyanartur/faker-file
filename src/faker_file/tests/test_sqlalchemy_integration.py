# from typing import Callable
# from unittest import TestCase, skip
#
# import sqlalchemy_factories as factories
# from faker import Faker
# from faker_file_admin import app
# from faker_file_admin.models import Upload
# from parametrize import parametrize
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# from ..storages.filesystem import FileSystemStorage
#
# __author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
# __copyright__ = "2022 Artur Barseghyan"
# __license__ = "MIT"
# __all__ = ("SQLAlchemyIntegrationTestCase",)
#
#
# STORAGE = FileSystemStorage(root_path="", rel_path="tmp")
#
#
# class SQLAlchemyIntegrationTestCase(TestCase):
#     """SQLAlchemy integration test case."""
#
#     engine = create_engine("sqlite:///:memory:")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#
#     def setUp(self: "SQLAlchemyIntegrationTestCase"):
#         Upload.metadata.create_all(self.engine)
#         self.session.commit()
#
#     def tearDown(self: "SQLAlchemyIntegrationTestCase"):
#         Upload.metadata.drop_all(self.engine)
#
#     FAKER: Faker
#
#     @parametrize(
#         "factory",
#         [
#             (factories.DocxUploadFactory,),
#             (factories.PdfUploadFactory,),
#             (factories.PptxUploadFactory,),
#             (factories.TxtUploadFactory,),
#             (factories.ZipUploadFactory,),
#         ],
#     )
#     @skip
#     def test_file(
#         self: "SQLAlchemyIntegrationTestCase", factory: Callable
#     ) -> None:
#         """Test file."""
#         with app.app_context():
#             _upload = factory()
#             self.session.commit()
#             self.assertTrue(STORAGE.exists(_upload.file))
