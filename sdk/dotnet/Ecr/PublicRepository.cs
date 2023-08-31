// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecr
{
    /// <summary>
    /// The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR
    /// </summary>
    [Obsolete(@"PublicRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ecr:PublicRepository")]
    public partial class PublicRepository : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see &lt;link&gt;
        /// </summary>
        [Output("repositoryCatalogData")]
        public Output<Outputs.RepositoryCatalogDataProperties?> RepositoryCatalogData { get; private set; } = null!;

        /// <summary>
        /// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        /// </summary>
        [Output("repositoryName")]
        public Output<string?> RepositoryName { get; private set; } = null!;

        /// <summary>
        /// The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 
        /// </summary>
        [Output("repositoryPolicyText")]
        public Output<object?> RepositoryPolicyText { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.PublicRepositoryTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a PublicRepository resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PublicRepository(string name, PublicRepositoryArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ecr:PublicRepository", name, args ?? new PublicRepositoryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PublicRepository(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ecr:PublicRepository", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "repositoryName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PublicRepository resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PublicRepository Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PublicRepository(name, id, options);
        }
    }

    public sealed class PublicRepositoryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see &lt;link&gt;
        /// </summary>
        [Input("repositoryCatalogData")]
        public Input<Inputs.RepositoryCatalogDataPropertiesArgs>? RepositoryCatalogData { get; set; }

        /// <summary>
        /// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        /// </summary>
        [Input("repositoryName")]
        public Input<string>? RepositoryName { get; set; }

        /// <summary>
        /// The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 
        /// </summary>
        [Input("repositoryPolicyText")]
        public Input<object>? RepositoryPolicyText { get; set; }

        [Input("tags")]
        private InputList<Inputs.PublicRepositoryTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.PublicRepositoryTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.PublicRepositoryTagArgs>());
            set => _tags = value;
        }

        public PublicRepositoryArgs()
        {
        }
        public static new PublicRepositoryArgs Empty => new PublicRepositoryArgs();
    }
}
