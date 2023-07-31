// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail.Inputs
{

    /// <summary>
    /// Describes the cache settings of an Amazon Lightsail content delivery network (CDN) distribution.
    /// </summary>
    public sealed class DistributionCacheSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The HTTP methods that are processed and forwarded to the distribution's origin.
        /// </summary>
        [Input("allowedHttpMethods")]
        public Input<string>? AllowedHttpMethods { get; set; }

        /// <summary>
        /// The HTTP method responses that are cached by your distribution.
        /// </summary>
        [Input("cachedHttpMethods")]
        public Input<string>? CachedHttpMethods { get; set; }

        /// <summary>
        /// The default amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the content has been updated.
        /// </summary>
        [Input("defaultTtl")]
        public Input<int>? DefaultTtl { get; set; }

        /// <summary>
        /// An object that describes the cookies that are forwarded to the origin. Your content is cached based on the cookies that are forwarded.
        /// </summary>
        [Input("forwardedCookies")]
        public Input<Inputs.DistributionCookieObjectArgs>? ForwardedCookies { get; set; }

        /// <summary>
        /// An object that describes the headers that are forwarded to the origin. Your content is cached based on the headers that are forwarded.
        /// </summary>
        [Input("forwardedHeaders")]
        public Input<Inputs.DistributionHeaderObjectArgs>? ForwardedHeaders { get; set; }

        /// <summary>
        /// An object that describes the query strings that are forwarded to the origin. Your content is cached based on the query strings that are forwarded.
        /// </summary>
        [Input("forwardedQueryStrings")]
        public Input<Inputs.DistributionQueryStringObjectArgs>? ForwardedQueryStrings { get; set; }

        /// <summary>
        /// The maximum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.
        /// </summary>
        [Input("maximumTtl")]
        public Input<int>? MaximumTtl { get; set; }

        /// <summary>
        /// The minimum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.
        /// </summary>
        [Input("minimumTtl")]
        public Input<int>? MinimumTtl { get; set; }

        public DistributionCacheSettingsArgs()
        {
        }
        public static new DistributionCacheSettingsArgs Empty => new DistributionCacheSettingsArgs();
    }
}
