// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync
{
    /// <summary>
    /// Resource Type definition for AWS::AppSync::Resolver
    /// </summary>
    [Obsolete(@"Resolver is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appsync:Resolver")]
    public partial class Resolver : global::Pulumi.CustomResource
    {
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("cachingConfig")]
        public Output<Outputs.ResolverCachingConfig?> CachingConfig { get; private set; } = null!;

        [Output("code")]
        public Output<string?> Code { get; private set; } = null!;

        [Output("codeS3Location")]
        public Output<string?> CodeS3Location { get; private set; } = null!;

        [Output("dataSourceName")]
        public Output<string?> DataSourceName { get; private set; } = null!;

        [Output("fieldName")]
        public Output<string> FieldName { get; private set; } = null!;

        [Output("kind")]
        public Output<string?> Kind { get; private set; } = null!;

        [Output("maxBatchSize")]
        public Output<int?> MaxBatchSize { get; private set; } = null!;

        [Output("pipelineConfig")]
        public Output<Outputs.ResolverPipelineConfig?> PipelineConfig { get; private set; } = null!;

        [Output("requestMappingTemplate")]
        public Output<string?> RequestMappingTemplate { get; private set; } = null!;

        [Output("requestMappingTemplateS3Location")]
        public Output<string?> RequestMappingTemplateS3Location { get; private set; } = null!;

        [Output("resolverArn")]
        public Output<string> ResolverArn { get; private set; } = null!;

        [Output("responseMappingTemplate")]
        public Output<string?> ResponseMappingTemplate { get; private set; } = null!;

        [Output("responseMappingTemplateS3Location")]
        public Output<string?> ResponseMappingTemplateS3Location { get; private set; } = null!;

        [Output("runtime")]
        public Output<Outputs.ResolverAppSyncRuntime?> Runtime { get; private set; } = null!;

        [Output("syncConfig")]
        public Output<Outputs.ResolverSyncConfig?> SyncConfig { get; private set; } = null!;

        [Output("typeName")]
        public Output<string> TypeName { get; private set; } = null!;


        /// <summary>
        /// Create a Resolver resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Resolver(string name, ResolverArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appsync:Resolver", name, args ?? new ResolverArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Resolver(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appsync:Resolver", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "apiId",
                    "fieldName",
                    "typeName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Resolver resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Resolver Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Resolver(name, id, options);
        }
    }

    public sealed class ResolverArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("cachingConfig")]
        public Input<Inputs.ResolverCachingConfigArgs>? CachingConfig { get; set; }

        [Input("code")]
        public Input<string>? Code { get; set; }

        [Input("codeS3Location")]
        public Input<string>? CodeS3Location { get; set; }

        [Input("dataSourceName")]
        public Input<string>? DataSourceName { get; set; }

        [Input("fieldName", required: true)]
        public Input<string> FieldName { get; set; } = null!;

        [Input("kind")]
        public Input<string>? Kind { get; set; }

        [Input("maxBatchSize")]
        public Input<int>? MaxBatchSize { get; set; }

        [Input("pipelineConfig")]
        public Input<Inputs.ResolverPipelineConfigArgs>? PipelineConfig { get; set; }

        [Input("requestMappingTemplate")]
        public Input<string>? RequestMappingTemplate { get; set; }

        [Input("requestMappingTemplateS3Location")]
        public Input<string>? RequestMappingTemplateS3Location { get; set; }

        [Input("responseMappingTemplate")]
        public Input<string>? ResponseMappingTemplate { get; set; }

        [Input("responseMappingTemplateS3Location")]
        public Input<string>? ResponseMappingTemplateS3Location { get; set; }

        [Input("runtime")]
        public Input<Inputs.ResolverAppSyncRuntimeArgs>? Runtime { get; set; }

        [Input("syncConfig")]
        public Input<Inputs.ResolverSyncConfigArgs>? SyncConfig { get; set; }

        [Input("typeName", required: true)]
        public Input<string> TypeName { get; set; } = null!;

        public ResolverArgs()
        {
        }
        public static new ResolverArgs Empty => new ResolverArgs();
    }
}
