// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CustomerProfiles.Inputs
{

    /// <summary>
    /// Represents a field in a ProfileObjectType.
    /// </summary>
    public sealed class ObjectTypeObjectTypeFieldArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content type of the field. Used for determining equality when searching.
        /// </summary>
        [Input("contentType")]
        public Input<Pulumi.AwsNative.CustomerProfiles.ObjectTypeObjectTypeFieldContentType>? ContentType { get; set; }

        /// <summary>
        /// A field of a ProfileObject. For example: _source.FirstName, where "_source" is a ProfileObjectType of a Zendesk user and "FirstName" is a field in that ObjectType.
        /// </summary>
        [Input("source")]
        public Input<string>? Source { get; set; }

        /// <summary>
        /// The location of the data in the standard ProfileObject model. For example: _profile.Address.PostalCode.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        public ObjectTypeObjectTypeFieldArgs()
        {
        }
    }
}
