// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena
{
    /// <summary>
    /// Resource schema for AWS::Athena::DataCatalog
    /// </summary>
    [AwsNativeResourceType("aws-native:athena:DataCatalog")]
    public partial class DataCatalog : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A description of the data catalog to be created. 
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. 
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. 
        /// </summary>
        [Output("parameters")]
        public Output<object?> Parameters { get; private set; } = null!;

        /// <summary>
        /// A list of comma separated tags to add to the data catalog that is created. 
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DataCatalogTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. 
        /// </summary>
        [Output("type")]
        public Output<Pulumi.AwsNative.Athena.DataCatalogType> Type { get; private set; } = null!;


        /// <summary>
        /// Create a DataCatalog resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataCatalog(string name, DataCatalogArgs args, CustomResourceOptions? options = null)
            : base("aws-native:athena:DataCatalog", name, args ?? new DataCatalogArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataCatalog(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:athena:DataCatalog", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataCatalog resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataCatalog Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataCatalog(name, id, options);
        }
    }

    public sealed class DataCatalogArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the data catalog to be created. 
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. 
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. 
        /// </summary>
        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        [Input("tags")]
        private InputList<Inputs.DataCatalogTagArgs>? _tags;

        /// <summary>
        /// A list of comma separated tags to add to the data catalog that is created. 
        /// </summary>
        public InputList<Inputs.DataCatalogTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DataCatalogTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. 
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.Athena.DataCatalogType> Type { get; set; } = null!;

        public DataCatalogArgs()
        {
        }
        public static new DataCatalogArgs Empty => new DataCatalogArgs();
    }
}
