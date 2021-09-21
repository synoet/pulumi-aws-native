// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ServiceCatalog
{
    /// <summary>
    /// Resource Type definition for AWS::ServiceCatalog::LaunchNotificationConstraint
    /// </summary>
    [Obsolete(@"LaunchNotificationConstraint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:servicecatalog:LaunchNotificationConstraint")]
    public partial class LaunchNotificationConstraint : Pulumi.CustomResource
    {
        [Output("acceptLanguage")]
        public Output<string?> AcceptLanguage { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("notificationArns")]
        public Output<ImmutableArray<string>> NotificationArns { get; private set; } = null!;

        [Output("portfolioId")]
        public Output<string> PortfolioId { get; private set; } = null!;

        [Output("productId")]
        public Output<string> ProductId { get; private set; } = null!;


        /// <summary>
        /// Create a LaunchNotificationConstraint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LaunchNotificationConstraint(string name, LaunchNotificationConstraintArgs args, CustomResourceOptions? options = null)
            : base("aws-native:servicecatalog:LaunchNotificationConstraint", name, args ?? new LaunchNotificationConstraintArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LaunchNotificationConstraint(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:servicecatalog:LaunchNotificationConstraint", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing LaunchNotificationConstraint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LaunchNotificationConstraint Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LaunchNotificationConstraint(name, id, options);
        }
    }

    public sealed class LaunchNotificationConstraintArgs : Pulumi.ResourceArgs
    {
        [Input("acceptLanguage")]
        public Input<string>? AcceptLanguage { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("notificationArns", required: true)]
        private InputList<string>? _notificationArns;
        public InputList<string> NotificationArns
        {
            get => _notificationArns ?? (_notificationArns = new InputList<string>());
            set => _notificationArns = value;
        }

        [Input("portfolioId", required: true)]
        public Input<string> PortfolioId { get; set; } = null!;

        [Input("productId", required: true)]
        public Input<string> ProductId { get; set; } = null!;

        public LaunchNotificationConstraintArgs()
        {
        }
    }
}
