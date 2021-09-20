// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ImageBuilder
{
    /// <summary>
    /// Resource schema for AWS::ImageBuilder::ContainerRecipe
    /// </summary>
    [AwsNativeResourceType("aws-native:imagebuilder:ContainerRecipe")]
    public partial class ContainerRecipe : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the container recipe.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Components for build and test that are included in the container recipe.
        /// </summary>
        [Output("components")]
        public Output<ImmutableArray<Outputs.ContainerRecipeComponentConfiguration>> Components { get; private set; } = null!;

        /// <summary>
        /// Specifies the type of container, such as Docker.
        /// </summary>
        [Output("containerType")]
        public Output<Pulumi.AwsNative.ImageBuilder.ContainerRecipeContainerType?> ContainerType { get; private set; } = null!;

        /// <summary>
        /// The description of the container recipe.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
        /// </summary>
        [Output("dockerfileTemplateData")]
        public Output<string?> DockerfileTemplateData { get; private set; } = null!;

        /// <summary>
        /// The S3 URI for the Dockerfile that will be used to build your container image.
        /// </summary>
        [Output("dockerfileTemplateUri")]
        public Output<string?> DockerfileTemplateUri { get; private set; } = null!;

        /// <summary>
        /// Specifies the operating system version for the source image.
        /// </summary>
        [Output("imageOsVersionOverride")]
        public Output<string?> ImageOsVersionOverride { get; private set; } = null!;

        /// <summary>
        /// A group of options that can be used to configure an instance for building and testing container images.
        /// </summary>
        [Output("instanceConfiguration")]
        public Output<Outputs.ContainerRecipeInstanceConfiguration?> InstanceConfiguration { get; private set; } = null!;

        /// <summary>
        /// Identifies which KMS key is used to encrypt the container image.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The name of the container recipe.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The source image for the container recipe.
        /// </summary>
        [Output("parentImage")]
        public Output<string?> ParentImage { get; private set; } = null!;

        /// <summary>
        /// Specifies the operating system platform when you use a custom source image.
        /// </summary>
        [Output("platformOverride")]
        public Output<Pulumi.AwsNative.ImageBuilder.ContainerRecipePlatformOverride?> PlatformOverride { get; private set; } = null!;

        /// <summary>
        /// Tags that are attached to the container recipe.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        /// <summary>
        /// The destination repository for the container image.
        /// </summary>
        [Output("targetRepository")]
        public Output<Outputs.ContainerRecipeTargetContainerRepository?> TargetRepository { get; private set; } = null!;

        /// <summary>
        /// The semantic version of the container recipe (&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;).
        /// </summary>
        [Output("version")]
        public Output<string?> Version { get; private set; } = null!;

        /// <summary>
        /// The working directory to be used during build and test workflows.
        /// </summary>
        [Output("workingDirectory")]
        public Output<string?> WorkingDirectory { get; private set; } = null!;


        /// <summary>
        /// Create a ContainerRecipe resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ContainerRecipe(string name, ContainerRecipeArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:imagebuilder:ContainerRecipe", name, args ?? new ContainerRecipeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ContainerRecipe(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:imagebuilder:ContainerRecipe", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ContainerRecipe resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ContainerRecipe Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ContainerRecipe(name, id, options);
        }
    }

    public sealed class ContainerRecipeArgs : Pulumi.ResourceArgs
    {
        [Input("components")]
        private InputList<Inputs.ContainerRecipeComponentConfigurationArgs>? _components;

        /// <summary>
        /// Components for build and test that are included in the container recipe.
        /// </summary>
        public InputList<Inputs.ContainerRecipeComponentConfigurationArgs> Components
        {
            get => _components ?? (_components = new InputList<Inputs.ContainerRecipeComponentConfigurationArgs>());
            set => _components = value;
        }

        /// <summary>
        /// Specifies the type of container, such as Docker.
        /// </summary>
        [Input("containerType")]
        public Input<Pulumi.AwsNative.ImageBuilder.ContainerRecipeContainerType>? ContainerType { get; set; }

        /// <summary>
        /// The description of the container recipe.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
        /// </summary>
        [Input("dockerfileTemplateData")]
        public Input<string>? DockerfileTemplateData { get; set; }

        /// <summary>
        /// The S3 URI for the Dockerfile that will be used to build your container image.
        /// </summary>
        [Input("dockerfileTemplateUri")]
        public Input<string>? DockerfileTemplateUri { get; set; }

        /// <summary>
        /// Specifies the operating system version for the source image.
        /// </summary>
        [Input("imageOsVersionOverride")]
        public Input<string>? ImageOsVersionOverride { get; set; }

        /// <summary>
        /// A group of options that can be used to configure an instance for building and testing container images.
        /// </summary>
        [Input("instanceConfiguration")]
        public Input<Inputs.ContainerRecipeInstanceConfigurationArgs>? InstanceConfiguration { get; set; }

        /// <summary>
        /// Identifies which KMS key is used to encrypt the container image.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The name of the container recipe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The source image for the container recipe.
        /// </summary>
        [Input("parentImage")]
        public Input<string>? ParentImage { get; set; }

        /// <summary>
        /// Specifies the operating system platform when you use a custom source image.
        /// </summary>
        [Input("platformOverride")]
        public Input<Pulumi.AwsNative.ImageBuilder.ContainerRecipePlatformOverride>? PlatformOverride { get; set; }

        /// <summary>
        /// Tags that are attached to the container recipe.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        /// <summary>
        /// The destination repository for the container image.
        /// </summary>
        [Input("targetRepository")]
        public Input<Inputs.ContainerRecipeTargetContainerRepositoryArgs>? TargetRepository { get; set; }

        /// <summary>
        /// The semantic version of the container recipe (&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;).
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        /// <summary>
        /// The working directory to be used during build and test workflows.
        /// </summary>
        [Input("workingDirectory")]
        public Input<string>? WorkingDirectory { get; set; }

        public ContainerRecipeArgs()
        {
        }
    }
}
