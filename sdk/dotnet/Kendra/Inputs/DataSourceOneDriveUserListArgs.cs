// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Kendra.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveuserlist.html
    /// </summary>
    public sealed class DataSourceOneDriveUserListArgs : Pulumi.ResourceArgs
    {
        [Input("OneDriveUserList")]
        private InputList<string>? _OneDriveUserList;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveuserlist.html#cfn-kendra-datasource-onedriveuserlist-onedriveuserlist
        /// </summary>
        public InputList<string> OneDriveUserList
        {
            get => _OneDriveUserList ?? (_OneDriveUserList = new InputList<string>());
            set => _OneDriveUserList = value;
        }

        public DataSourceOneDriveUserListArgs()
        {
        }
    }
}