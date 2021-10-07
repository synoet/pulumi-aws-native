// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Backup::BackupSelection
type BackupSelection struct {
	pulumi.CustomResourceState

	BackupPlanId    pulumi.StringOutput               `pulumi:"backupPlanId"`
	BackupSelection BackupSelectionResourceTypeOutput `pulumi:"backupSelection"`
	SelectionId     pulumi.StringOutput               `pulumi:"selectionId"`
}

// NewBackupSelection registers a new resource with the given unique name, arguments, and options.
func NewBackupSelection(ctx *pulumi.Context,
	name string, args *BackupSelectionArgs, opts ...pulumi.ResourceOption) (*BackupSelection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BackupSelection == nil {
		return nil, errors.New("invalid value for required argument 'BackupSelection'")
	}
	var resource BackupSelection
	err := ctx.RegisterResource("aws-native:backup:BackupSelection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBackupSelection gets an existing BackupSelection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBackupSelection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BackupSelectionState, opts ...pulumi.ResourceOption) (*BackupSelection, error) {
	var resource BackupSelection
	err := ctx.ReadResource("aws-native:backup:BackupSelection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BackupSelection resources.
type backupSelectionState struct {
}

type BackupSelectionState struct {
}

func (BackupSelectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*backupSelectionState)(nil)).Elem()
}

type backupSelectionArgs struct {
	BackupSelection BackupSelectionResourceType `pulumi:"backupSelection"`
}

// The set of arguments for constructing a BackupSelection resource.
type BackupSelectionArgs struct {
	BackupSelection BackupSelectionResourceTypeInput
}

func (BackupSelectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*backupSelectionArgs)(nil)).Elem()
}

type BackupSelectionInput interface {
	pulumi.Input

	ToBackupSelectionOutput() BackupSelectionOutput
	ToBackupSelectionOutputWithContext(ctx context.Context) BackupSelectionOutput
}

func (*BackupSelection) ElementType() reflect.Type {
	return reflect.TypeOf((*BackupSelection)(nil))
}

func (i *BackupSelection) ToBackupSelectionOutput() BackupSelectionOutput {
	return i.ToBackupSelectionOutputWithContext(context.Background())
}

func (i *BackupSelection) ToBackupSelectionOutputWithContext(ctx context.Context) BackupSelectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BackupSelectionOutput)
}

type BackupSelectionOutput struct{ *pulumi.OutputState }

func (BackupSelectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*BackupSelection)(nil))
}

func (o BackupSelectionOutput) ToBackupSelectionOutput() BackupSelectionOutput {
	return o
}

func (o BackupSelectionOutput) ToBackupSelectionOutputWithContext(ctx context.Context) BackupSelectionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(BackupSelectionOutput{})
}
