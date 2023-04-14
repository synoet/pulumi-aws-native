// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager.Inputs
{

    /// <summary>
    /// The location of the site
    /// </summary>
    public sealed class SiteLocationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The physical address.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The latitude.
        /// </summary>
        [Input("latitude")]
        public Input<string>? Latitude { get; set; }

        /// <summary>
        /// The longitude.
        /// </summary>
        [Input("longitude")]
        public Input<string>? Longitude { get; set; }

        public SiteLocationArgs()
        {
        }
        public static new SiteLocationArgs Empty => new SiteLocationArgs();
    }
}
