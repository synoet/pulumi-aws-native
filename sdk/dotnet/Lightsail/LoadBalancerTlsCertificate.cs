// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    /// <summary>
    /// Resource Type definition for AWS::Lightsail::LoadBalancerTlsCertificate
    /// </summary>
    [AwsNativeResourceType("aws-native:lightsail:LoadBalancerTlsCertificate")]
    public partial class LoadBalancerTlsCertificate : Pulumi.CustomResource
    {
        /// <summary>
        /// An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.
        /// </summary>
        [Output("certificateAlternativeNames")]
        public Output<ImmutableArray<string>> CertificateAlternativeNames { get; private set; } = null!;

        /// <summary>
        /// The domain name (e.g., example.com ) for your SSL/TLS certificate.
        /// </summary>
        [Output("certificateDomainName")]
        public Output<string> CertificateDomainName { get; private set; } = null!;

        /// <summary>
        /// The SSL/TLS certificate name.
        /// </summary>
        [Output("certificateName")]
        public Output<string> CertificateName { get; private set; } = null!;

        /// <summary>
        /// A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
        /// </summary>
        [Output("httpsRedirectionEnabled")]
        public Output<bool?> HttpsRedirectionEnabled { get; private set; } = null!;

        /// <summary>
        /// When true, the SSL/TLS certificate is attached to the Lightsail load balancer.
        /// </summary>
        [Output("isAttached")]
        public Output<bool?> IsAttached { get; private set; } = null!;

        /// <summary>
        /// The name of your load balancer.
        /// </summary>
        [Output("loadBalancerName")]
        public Output<string> LoadBalancerName { get; private set; } = null!;

        [Output("loadBalancerTlsCertificateArn")]
        public Output<string> LoadBalancerTlsCertificateArn { get; private set; } = null!;

        /// <summary>
        /// The validation status of the SSL/TLS certificate.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;


        /// <summary>
        /// Create a LoadBalancerTlsCertificate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadBalancerTlsCertificate(string name, LoadBalancerTlsCertificateArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:LoadBalancerTlsCertificate", name, args ?? new LoadBalancerTlsCertificateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoadBalancerTlsCertificate(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:LoadBalancerTlsCertificate", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing LoadBalancerTlsCertificate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadBalancerTlsCertificate Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LoadBalancerTlsCertificate(name, id, options);
        }
    }

    public sealed class LoadBalancerTlsCertificateArgs : Pulumi.ResourceArgs
    {
        [Input("certificateAlternativeNames")]
        private InputList<string>? _certificateAlternativeNames;

        /// <summary>
        /// An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.
        /// </summary>
        public InputList<string> CertificateAlternativeNames
        {
            get => _certificateAlternativeNames ?? (_certificateAlternativeNames = new InputList<string>());
            set => _certificateAlternativeNames = value;
        }

        /// <summary>
        /// The domain name (e.g., example.com ) for your SSL/TLS certificate.
        /// </summary>
        [Input("certificateDomainName", required: true)]
        public Input<string> CertificateDomainName { get; set; } = null!;

        /// <summary>
        /// The SSL/TLS certificate name.
        /// </summary>
        [Input("certificateName", required: true)]
        public Input<string> CertificateName { get; set; } = null!;

        /// <summary>
        /// A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
        /// </summary>
        [Input("httpsRedirectionEnabled")]
        public Input<bool>? HttpsRedirectionEnabled { get; set; }

        /// <summary>
        /// When true, the SSL/TLS certificate is attached to the Lightsail load balancer.
        /// </summary>
        [Input("isAttached")]
        public Input<bool>? IsAttached { get; set; }

        /// <summary>
        /// The name of your load balancer.
        /// </summary>
        [Input("loadBalancerName", required: true)]
        public Input<string> LoadBalancerName { get; set; } = null!;

        public LoadBalancerTlsCertificateArgs()
        {
        }
    }
}
