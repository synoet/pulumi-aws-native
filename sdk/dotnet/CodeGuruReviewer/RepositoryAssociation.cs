// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeGuruReviewer
{
    /// <summary>
    /// This resource schema represents the RepositoryAssociation resource in the Amazon CodeGuru Reviewer service.
    /// </summary>
    [AwsNativeResourceType("aws-native:codegurureviewer:RepositoryAssociation")]
    public partial class RepositoryAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the repository association.
        /// </summary>
        [Output("associationArn")]
        public Output<string> AssociationArn { get; private set; } = null!;

        /// <summary>
        /// The name of the S3 bucket associated with an associated S3 repository. It must start with `codeguru-reviewer-`.
        /// </summary>
        [Output("bucketName")]
        public Output<string?> BucketName { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.
        /// </summary>
        [Output("connectionArn")]
        public Output<string?> ConnectionArn { get; private set; } = null!;

        /// <summary>
        /// Name of the repository to be associated.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The owner of the repository. For a Bitbucket repository, this is the username for the account that owns the repository.
        /// </summary>
        [Output("owner")]
        public Output<string?> Owner { get; private set; } = null!;

        /// <summary>
        /// The tags associated with a repository association.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.RepositoryAssociationTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The type of repository to be associated.
        /// </summary>
        [Output("type")]
        public Output<Pulumi.AwsNative.CodeGuruReviewer.RepositoryAssociationType> Type { get; private set; } = null!;


        /// <summary>
        /// Create a RepositoryAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RepositoryAssociation(string name, RepositoryAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:codegurureviewer:RepositoryAssociation", name, args ?? new RepositoryAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RepositoryAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:codegurureviewer:RepositoryAssociation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RepositoryAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RepositoryAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new RepositoryAssociation(name, id, options);
        }
    }

    public sealed class RepositoryAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the S3 bucket associated with an associated S3 repository. It must start with `codeguru-reviewer-`.
        /// </summary>
        [Input("bucketName")]
        public Input<string>? BucketName { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.
        /// </summary>
        [Input("connectionArn")]
        public Input<string>? ConnectionArn { get; set; }

        /// <summary>
        /// Name of the repository to be associated.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The owner of the repository. For a Bitbucket repository, this is the username for the account that owns the repository.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("tags")]
        private InputList<Inputs.RepositoryAssociationTagArgs>? _tags;

        /// <summary>
        /// The tags associated with a repository association.
        /// </summary>
        public InputList<Inputs.RepositoryAssociationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.RepositoryAssociationTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The type of repository to be associated.
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.CodeGuruReviewer.RepositoryAssociationType> Type { get; set; } = null!;

        public RepositoryAssociationArgs()
        {
        }
    }
}
